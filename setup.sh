#!/bin/bash

echo command[check_pods]=/usr/lib64/nagios/plugins/kubernetes-checks/nagios_check.sh pod >> /etc/nagios/nrpe.cfg 
command[check_nodes]=/usr/lib64/nagios/plugins/kubernetes-checks/nagios_check.sh node    >> /etc/nagios/nrpe.cfg


systemctl restart nrpe

cat /etc/nagios/nrpe.cfg
