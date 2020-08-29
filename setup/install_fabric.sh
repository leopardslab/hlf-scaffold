#!/bin/bash

if [ -z $SUDO_USER ]
then
    echo "Please run the command using sudo"
    echo "Usage: sudo ./docker.sh"
    exit 0
fi

# if [ -z $GOPATH ]; then
#     echo "GOPATH not set!!! Please set the Go Path"
#     echo "Aborting!!!"
#     exit 0
# fi


export PATH=$PATH:$GOROOT/bin

echo "GOROOT=$GOROOT"


mkdir temp  &> /dev/null
cd temp
echo "__________Downloading Fabric____________"
curl -sSL http://bit.ly/2ysbOFE -o bootstrap.sh
chmod 755 ./bootstrap.sh
bash ./bootstrap.sh -- 2.0.1 1.4.6 0.4.18

# Copying binaries
cp ./fabric-samples/bin/*    /usr/local/bin

# Clean up
cd ..
rm -rf  temp