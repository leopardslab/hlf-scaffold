#!/bin/bash

if [ -z $SUDO_USER ]
then
    echo "Please run the command using sudo"
    echo "Usage: sudo ./docker.sh"
    exit 0
fi


wget https://dl.google.com/go/go1.13.3.linux-amd64.tar.gz
act='ttyout="*"'
tar -xf go1.13.3.linux-amd64.tar.gz --checkpoint --checkpoint-action=$act -C /usr/local 
rm go1.13.3.linux-amd64.tar.gz



echo "export GOROOT=/usr/local/go" >> ~/.profile
echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.profile
echo "export GOROOT=/usr/local/go" >> ~/.bashrc

GOPATH=${1:-$PWD} 
echo $GOPATH
echo "export GOPATH=$GOPATH" >> ~/.profile
echo "export GOPATH=$GOPATH" >> ~/.bashrc

source ~/.profile
source ~/.bashrc