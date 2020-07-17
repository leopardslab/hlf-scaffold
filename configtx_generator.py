import yaml
import os
import copy
import json


class Configtx:
    def __init__(self, peer_orgs, order_orgs, orderer_nodes, domain='example.com'):

        with open('./assets/configtx.json') as json_file:
            self.configtx_template = json.load(json_file)

        self.no_of_peer_orgs = peer_orgs
        self.no_of_orderer_orgs = order_orgs
        self.domain = domain
        self.base_port = 7050
        self.oderer_nodes = orderer_nodes

    def generate_default(self):
        self.configtx_template["Organizations"] = []
        for i in range(self.no_of_orderer_orgs):
            if i == 0:
                self.configtx_template["Organizations"].append({
                        "Name": "OrdererOrg",
                        "ID": "OrdererMSP",
                        "MSPDir": "crypto-config/ordererOrganizations/{0}/msp".format(self.domain),
                        "Policies": {
                                        "Readers": {
                                          "Type": "Signature",
                                          "Rule": "OR('OrdererMSP.member')"
                                        },
                                        "Writers": {
                                          "Type": "Signature",
                                          "Rule": "OR('OrdererMSP.member')"
                                        },
                                        "Admins": {
                                          "Type": "Signature",
                                          "Rule": "OR('OrdererMSP.admin')"
                                        }
                                        }})
        for j in range(self.no_of_peer_orgs):
            id = "Org{0}MPS".format(j+1)
            host = "peer{0}.{1}.{2}".format(0, "org{0}".format(j), self.domain)
            port = self.base_port
            self.configtx_template["Organizations"].append(
                {
                    "Name": id,
                    "ID": host,
                    "MSPDir": "crypto-config/peerOrganizations/{0}/msp".format(host),
                    "Policies": {
                        "Readers": {
                            "Type": "Signature",
                            "Rule": "OR('{0}.admin', '{0}.peer', '{0}.client')".format(id)
                        },
                        "Writers": {
                            "Type": "Signature",
                            "Rule": "OR('{0}.admin', '{0}.client')".format(id)
                        },
                        "Admins": {
                            "Type": "Signature",
                            "Rule": "OR('{0}.admin')".format(id)
                        },
                        "Endorsement": {
                            "Type": "Signature",
                            "Rule": "OR('{0}.peer')".format(id)
                        }
                    },
                    "AnchorPeers": [
                        {
                            "Host": host,
                            "Port": port+(1000*i)+1
                        }
                    ]
                })

        self.config_orderers()
        self.config_profiles()

        print(self.configtx_template)

    def config_orderers(self):
        Consenters = [
            {
                "Host": "orderer.{0}".format(self.domain),
                "Port": self.base_port,
                "ClientTLSCert": "crypto-config/ordererOrganizations/{0}/orderers/orderer.orderer.{0}/tls/server.crt".format(self.domain),
                "ServerTLSCert": "crypto-config/ordererOrganizations/[0]/orderers/orderer.{0}/tls/server.crt".format(self.domain)
            }
        ]

        self.configtx_template["Orderer"]["EtcdRaft"]["Consenters"] = Consenters

    def config_profiles(self):
        self.configtx_template["Profiles"]["BasicChannel"]["Application"]["Organizations"] = []

        for item in self.configtx_template["Organizations"]:
            if not('ordererOrganizations' in item["MSPDir"]):
                self.configtx_template["Profiles"]["BasicChannel"]["Application"]["Organizations"].append(item)

        self.configtx_template["Profiles"]["OrdererGenesis"]["Orderer"]["EtcdRaft"]["Consenterss"] = []
        self.configtx_template["Profiles"]["OrdererGenesis"]["Orderer"]["Addresses"] = []
        for i in range(self.oderer_nodes):
            self.configtx_template["Profiles"]["OrdererGenesis"]["Orderer"]["EtcdRaft"]["Consenters"].append( {
              "Host": "orderer{0}.{1}".format(i+1, self.domain),
              "Port": self.base_port+(1000*i),
              "ClientTLSCert": "crypto-config/ordererOrganizations/{0}/orderers/orderer{1}.{2}/tls/server.crt".format(self.domain, i+1, self.domain),
              "ServerTLSCert": "crypto-config/ordererOrganizations/{0}/orderers/orderer{1}.{2}/tls/server.crt".format(self.domain, i+1, self.domain)
            })

            self.configtx_template["Profiles"]["OrdererGenesis"]["Orderer"]["Addresses"].append("orderer{0}.{1}:{2}".format(i, self.domain, self.base_port+(1000*i)))

        self.configtx_template["Profiles"]["OrdererGenesis"]["Orderer"] = []
