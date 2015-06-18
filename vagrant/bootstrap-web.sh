#!/usr/bin/env bash

mkdir -p /home/vagrant/.ssh
chmod 700 /home/vagrant/.ssh
cat /vagrant/mgmt_id_rsa.pub >> /home/vagrant/.ssh/authorized_keys
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

