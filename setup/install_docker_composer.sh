#!/bin/bash

VERSION=${1:-1.26.0} 

sudo curl -L https://github.com/docker/compose/releases/download/$VERSION/docker-compose-$(uname -s)-$(uname -m) -o /usr/bin/docker-compose
 
sudo chmod +x /usr/bin/docker-compose
