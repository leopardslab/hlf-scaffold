import yaml
import os
import copy

class CryptoConfig:
    def __init__(self, orgs=1, ords=1):
        self.no_of_peer_orgs = orgs
        self.no_of_orderers = ords
        self.orgs=[]
        self.orders=[]
        self.template = {
            "OrdererOrgs": [],
            "PeerOrgs": []
        }
        self.ordererTemplate ={
            "Name": "Orderer",
            "Domain": "example.com",
            "EnableNodeOUs": True,
            "Specs": []
        }

        self.peerOrgTemplate = {
            "Name": "",
            "Domain": "",
            "EnableNodeOUs": True,
            "Template": {
              "Count": 2,
              "SANS": [
                "localhost"
              ]
            },
            "Users": {
              "Count": 1
            }
        }

        # path1 = os.getcwd()+'/network/'
        directory = os.getcwd()+'/network/config/'
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Creation of the directory %s failed" % directory)
        else:
            print("Successfully created the directory %s " % directory)

    def set_default_values(self):
        print("Populate the YAML file with default values")

        self.template["OrdererOrgs"].append(self.ordererTemplate)
        for i in range(self.no_of_orderers):
            self.template["OrdererOrgs"][0]["Specs"].append({"Hostname": "orderer" + str(i), "SANS": ["localhost","127.0.0.1"]})

        for i in range(self.no_of_peer_orgs):
            tmp = copy.deepcopy(self.peerOrgTemplate)
            self.template["PeerOrgs"].append(tmp)
            self.template["PeerOrgs"][i]["Name"] = "Org" + str(i+1)
            self.template["PeerOrgs"][i]["Domain"] = "org" + str(i+1) + ".example.com"

        with open('network/config/crypto-config.yaml', 'w') as f:
            data = yaml.dump(self.template, f)

    def add_org(self, name, domain, template_count):
        print(10)




