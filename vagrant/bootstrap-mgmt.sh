#!/usr/bin/env bash

# install ansible (http://docs.ansible.com/intro_installation.html)
apt-get -y install software-properties-common
apt-add-repository -y ppa:ansible/ansible
apt-get update
apt-get -y install ansible

# Creating ssh key
mkdir -p /home/vagrant/.ssh
chmod 700 /home/vagrant/.ssh
ssh-keygen -t rsa -b 2048 -N '' -f /home/vagrant/.ssh/id_rsa
cp /home/vagrant/.ssh/id_rsa.pub /vagrant/mgmt_id_rsa.pub

# copy examples into /home/vagrant (from inside the mgmt node)
cp -a /vagrant/mgmt/* /home/vagrant
chown -R vagrant:vagrant /home/vagrant

# configure hosts file for our internal network defined by Vagrantfile
cat >> /etc/hosts <<EOF

# vagrant environment nodes
10.0.15.10  mgmt
#10.0.15.11  lb
10.0.15.20  mongo
10.0.15.21  web1
10.0.15.22  web2
#10.0.15.23  web3
EOF

