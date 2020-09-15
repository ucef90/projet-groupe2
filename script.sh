#!/bin/bash

sudo apt update
sudo apt upgrade -y
sudo apt install -y python3 python3-pip virtualenv 
git clone https://github.com/fitec-hkhan/projet-groupe2.git
cd projet-groupe2
source venv/bin/activate
pip3 install -r requirements.txt
python3 scrapping.py