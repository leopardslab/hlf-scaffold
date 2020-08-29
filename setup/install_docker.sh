#!/bin/bash

if [ -z $SUDO_USER ]
then
    echo "Please run the command using sudo"
    echo "Usage: sudo ./docker.sh"
    exit 0
fi


DOCKER_VERSION=${1:-18.03} 


install(){
    apt-get update
    apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
    apt-key fingerprint 0EBFCD88
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    apt-get update
    apt-get install -y "docker-ce=${DOCKER_VERSION}.*"
    docker info
    echo "======= Adding $SUDO_USER to the docker group ======="
    usermod -aG docker $SUDO_USER
}


install
service docker restart
systemctl daemon-reload
systemctl restart docker