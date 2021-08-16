#!/bin/sh
sudo apt update
sudo apt upgrade -y
sudo apt-get install ansible -y
git clone https://github.com/siddhartha-12/Weather-App.git
pwd
cd Weather-App/Ansible
ansible-playbook applicationSetup.yml 

