#!/bin/sh
sudo apt-get install ansible
git clone https://github.com/siddhartha-12/Weather-App.git
cd Weather-App/Ansible
ansible-playbook applicationSetup.yml 
rm -rf Weather-App
