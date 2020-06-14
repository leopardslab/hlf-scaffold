#!/bin/bash

sudo apt update
sudo apt install nodejs -y

sudo apt install npm -y
nodejs -v


apt-get install g++ -y


cd ~
curl -sL https://deb.nodesource.com/setup_12.x -o nodesource_setup.sh

sudo bash nodesource_setup.sh
sudo apt install nodejs -y