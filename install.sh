#!/usr/bin/env bash


sudo apt-get install libffi-dev
sudo apt-get install libssl-dev
sudo apt-get install build-essential
sudo apt-get install python3.8-dev
sudo apt-get install libpython3-dev

pip3 uninstall Fabric # uninstall Fabric if any

pip3 install -r requirements.txt
