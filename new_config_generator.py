import sys
import ruamel.yaml 
from ruamel.yaml.anchor import Anchor
import copy
import json


class Configtx:
    def __init__(self, peer_orgs, order_orgs, orderer_nodes, domain='example.com'):

        with open('./assets/configtx.yaml') as yaml_file:
            self.configtx_template = ruamel.yaml.round_trip_load(yaml_file)

        self.no_of_peer_orgs = peer_orgs
        self.no_of_orderer_orgs = order_orgs
        self.domain = domain
        self.base_port = 7050
        self.oderer_nodes = orderer_nodes


        #print(help(org_template))
        self.generate_organizations_block()
        self.generate_orderer_block()
        

    def generate_organizations_block(self):
        for i in range(self.no_of_peer_orgs-2):   
            org_template = copy.deepcopy(self.configtx_template["Organizations"][1])
            org_name = "Org{0}".format(i+3)         
            self.configtx_template["Organizations"].append(org_template)
            data = self.configtx_template["Organizations"][i+3]
            data["Name"] = org_name + "MSP"
            data["ID"] = org_name + "MSP"
            data.yaml_set_anchor(org_name + "MSP")
            data["MSPDir"] = "crypto-config/peerOrganizations/{0}.{1}.com/msp".format(org_name.lower(), self.domain)

            data["Policies"]["Readers"]["Rule"] = "OR('{0}MSP.admin', '{0}MSP.peer', '{0}MSP.client')".format(org_name)
            data["Policies"]["Writers"]["Rule"] = "OR('{0}MSP.admin', '{0}MSP.client')".format(org_name)
            data["Policies"]["Admins"]["Rule"] = "OR('{0}MSP.admin')".format(org_name)
            data["Policies"]["Endorsement"]["Rule"] = "OR('{0}MSP.peer')".format(org_name)

            #print(data["AnchorPeers"])
            data["AnchorPeers"][0]["Host"] = "peer0.{0}.{1}.com".format(org_name.lower(), self.domain)
            data["AnchorPeers"][0]["Port"] = self.base_port + (1000*(i+2)) + 1

        with open('./assets/configtx_.yaml', "w") as f:
            ruamel.yaml.round_trip_dump(self.configtx_template, f)
    
    def generate_orderer_block(self):
        print(self.configtx_template["Orderer"]["EtcdRaft"])