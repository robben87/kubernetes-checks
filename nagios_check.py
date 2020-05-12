#!/usr/bin/env pipenv-shebang
import socket
import sys
import numpy as np
import pandas as pd
import argparse
import os
from tabulate import tabulate
from kubernetes import client, config

def load_configuration(configuration):
    config_dir = "~/.kube/"
    config_name= args.configfile
    kubeconfig = os.path.join(config_dir,config_name)
#    print(kubeconfig)
    config.load_kube_config(config_file=kubeconfig)

#Output Formatting
def pretty_print(df):
    print(tabulate(df, showindex=False, headers=df.columns, numalign="left"))


def check_node():
    configuration = args.configfile
    load_configuration(configuration)
    v1 = client.CoreV1Api()
    list_nodes = v1.list_node()
    #data = np.array([['','Name','Type','Status','Reason','Message']])
    data = pd.DataFrame(columns=['NAME','TYPE','STATUS','REASON','MESSAGE'])
    
    for node in list_nodes.items:
        name_list=node.metadata.name
        status_node = v1.read_node_status(name=name_list)
        condition=status_node.status.conditions
        for value in condition:
            name_node=status_node.metadata.name
            type_obj=value.type
            message=value.message
            status=value.status
            reason=value.reason
            if str(status) != "False" and str(type_obj) != "Ready" and  str(type_obj) != "OutOfDisk":
                        #data = np.append(data,[['',name_node,type_obj,status,reason,message]],axis=0)
                        data = data.append({'NAME': name_node,'TYPE': type_obj,'STATUS': status,'REASON': reason,'MESSAGE': message}, ignore_index=True)
            #df = pd.DataFrame(data=data[1:,0:],index=data[1:,0],columns=data[0,0:])
            output = data
    if data.empty:
        print("ALL NODES ARE OK")
        sys.exit(0);    
    else:
        pretty_print(output)
        sys.exit(1);  


def check_pod():
    configuration = args.configfile
    load_configuration(configuration)
    v1=client.CoreV1Api()
    ret = v1.list_pod_for_all_namespaces(watch=False)
    data = pd.DataFrame(columns=['NAMESPACE','NAME','STATUS','HOST','MESSAGE','REASON'])
    for pod in ret.items:
        if str(pod.status.phase) != "Running":
            if str(pod.status.phase) != "Succeeded":
                if str(pod.status.host_ip) == "None":
                    hostname = ""
                    pod.status.host_ip = ""
                else:
                    host_lookup = socket.gethostbyaddr(str(pod.status.host_ip))
                    hostname = host_lookup[0]
                #print("%s\t%s\t%s\t%s\t%s" % (pod.metadata.namespace, pod.metadata.name, pod.status.phase,hostname,pod.status.host_ip))
                if pod.status.message is None and pod.status.reason is None and pod.status.nominated_node_name is None:
                    pod.status.message = ""
                    pod.status.reason  = ""
                    if args.namespaceblacklist:
                        if pod.metadata.namespace == args.namespaceblacklist:
                            null = ""
                        else:
                            data = data.append({'NAMESPACE': pod.metadata.namespace,'NAME': pod.metadata.name,'STATUS': pod.status.phase,'HOST': hostname,'MESSAGE': pod.status.message,'REASON': pod.status.reason}, ignore_index=True)
                            output = data
                    else:
                        data = data.append({'NAMESPACE': pod.metadata.namespace,'NAME': pod.metadata.name,'STATUS': pod.status.phase,'HOST': hostname,'MESSAGE': pod.status.message,'REASON': pod.status.reason}, ignore_index=True)
                        output = data
    if data.empty:
        print("ALL PODS ARE OK")
        sys.exit(0);    
    else:
        pretty_print(output)
        sys.exit(1);

if __name__=='__main__':

    parser=argparse.ArgumentParser()
    subparsers=parser.add_subparsers()
    
    #createtheparserforthe"node"command
    parser_node=subparsers.add_parser("node",help="check_nodes status)")
    parser_node.add_argument("-conf","--configfile",help="Specify kubernetes config file name to load (default path is ~/.kube)",default="config")
    parser_node.set_defaults(func=check_node)
    #createtheparserforthe"pod"command
    parser_pod=subparsers.add_parser("pod",help="check_pods status")
    parser_pod.add_argument("-conf","--configfile",help="Specify kubernetes config file name to load (default path is ~/.kube)",default="config")
    parser_pod.add_argument("-nbl","--namespaceblacklist",help="Specify kubernetes config file name to load (default path is ~/.kube)",nargs='?', const="Y", type=str)
    parser_pod.set_defaults(func=check_pod)

    if len(sys.argv[1:])==0:
        parser.print_help()
    args=parser.parse_args()                                                               

    if "node" in sys.argv:
        check_node()
    elif "pod" in sys.argv:
        check_pod()
    else:
        print("For Sub-Commands Options use nagios_check.py argument -h")
