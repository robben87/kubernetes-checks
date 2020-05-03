#!/bin/bash
export PATH=/var/run/nrpe/.local/bin:/var/run/nrpe/.local/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin
export LANG=en_US.UTF-8

argument=$1
blacklist=$2
#configfilename=$2

if [[ -z $argument || -z $blacklist ]]
then
~/.local/bin/pipenv-shebang    /usr/lib64/nagios/plugins/kubernetes-checks/nagios_check.py $argument
else
~/.local/bin/pipenv-shebang    /usr/lib64/nagios/plugins/kubernetes-checks/nagios_check.py $argument --namespaceblacklist $blacklist
fi
