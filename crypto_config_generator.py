import yaml
import os

class CryptoConfig:

  def __init__(self, orgs=0, ords=0):
    self.no_of_orgs = orgs
    self.no_of_orderers = orgs
    self.orgs=[]
    self.orders=[]

    path1 = os.getcwd()+'/network/'
    directory = os.getcwd()+'/network/config/'
    try:
        os.mkdir(path1)
        os.mkdir(directory)
    except OSError:
        print ("Creation of the directory %s failed" % directory)
    else:
        print ("Successfully created the directory %s " % directory)

    

  def set_default_values(self):
    print("Populate the YAML file with default values")

    users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]

    with open('network/config/crypto-config.yaml', 'w') as f:
        data = yaml.dump(users, f)

  def add_org(self, name, domain, template_count):
      print(10)
