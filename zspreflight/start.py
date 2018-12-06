#! /usr/bin/env python
import getpass
import pprint
import paramiko
import re
import socket
import multiprocessing as mp
#from preflight import preflight as pf

def _get_customer():
    customer_name = raw_input("What is the organization name? ")
    customer_contact = raw_input("What is the customer contact email? ")

    #check if email is valid form
    print customer_contact
    try:
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', customer_contact) != None:
            print "The minimum ZeroStack cluster is 4 nodes, you do not need to have 4 nodes to run this test."
    except Exception as e:
        print "Invalid Email given, please enter a valid email address."
        _get_customer()

    return {'cn':customer_name,'cc':customer_contact}

def _get_node_ip():
    host_ip = raw_input("Please enter the node IP: ")
    try:
        socket.inet_aton(host_ip)
    except socket.error:
        "Invalid IP given"
        _get_node_ip()

    return host_ip

def _run_validation(input_dict,output):
    #establish a connection
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.WarningPolicy)
        client.connect(input_dict['host'], port='22', username=input_dict['user'], password=input_dict['password'])
        try:
            #pull the validator software to the target host
            stdin, stdout, stderr = client.exec_command('sudo pip install zs_preflight')
        except Exception as e:
            print "Could not pull files to target host %s."%(input_dict['host'])
            _run_validation(input_dict,output)

        try:
            #run the validator
            stdin, stdout, stderr = client.exec_command('zs-validate-host')
        except Exception as e:
            print "Could not pull files to target host %s."%(input_dict['host'])
            _run_validation(input_dict,output)
        output.put(stdout.read())
    except Exception as e:
        print "Could not establish connection to %s"%(input_dict['host'])
        _run_validation(input_dict,output)

    finally:
        client.close()

if __name__ == '__main__':
    print "ZeroStack pre-flight check system."
    proceed = raw_input("Do you want to proceed? (yes/no)")

    if(str(proceed).lower() == 'y' or str(proceed).lower() == 'yes'):
        #collect the host data
        cust = _get_customer()

        #get the host info
        hosts = []
        more_hosts = 'yes'
        while(str(more_hosts).lower() == 'y' or str(more_hosts).lower() == 'yes'):
            host = _get_node_ip()
            user = raw_input("Please enter the username for %s: "%(host))
            password = getpass.getpass("Please enter the password for %s: "%(host))
            hosts.append({'host':host,'user':user,'password':password})
            more_hosts = raw_input("Do you have more nodes to check? (Yes/No) ")

        output = mp.Queue()

        processes = [mp.Process(target=_run_validation, args=(hosts[x], output,)) for x in range(len(hosts))]
        for p in processes:
            p.start()

        for p in processes:
            p.join()

        results = [output.get() for p in processes]

        for result in results:
            print "-------------------------"
            print "\n"
            print result

    elif(str(proceed).lower() == 'n' or str(proceed).lower() == 'no'):
        print "Zerostack pre-flight is exiting, please run the pre-flight checklist before installing the ZCOS on this host(s)"
        exit

    else:
        print "Unknown input given."
        exit
