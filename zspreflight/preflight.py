#!/usr/bin/python
import os
from compute import compute_check
from network import network_check
from storage import storage_check
from host import host_check
import pprint

print "Zerostack pre-flight check system."
proceed = raw_input("Do you want to proceed? (yes/no)")

if(str(proceed).lower() == 'y' or str(proceed).lower() == 'yes'):
    overall_host_findings = {}
    overall_compute_findings = {}
    overall_net_findings = {}
    overall_storage_findings = {}

    cc = compute_check()
    hc = host_check()
    sc = storage_check()
    nc = network_check()

    #check the overall host
    overall_host_findings['host_cpu_architecture'] = cc.cpu_architecture()
    overall_host_findings['host_type'] = cc.cpu_virtualized()
    overall_host_findings['host_ipmi'] = hc.host_ipmi()
    overall_host_findings['host_usb'] = hc.host_usb()
    overall_host_findings['host_disks'] = sc.internal_drive_count()
    overall_host_findings['host_nics'] = nc.nic_count()
    #pprint.pprint(overall_host_findings)

    overall_compute_findings['compute_x86_64'] = cc.cpu_architecture()
    overall_compute_findings['compute_cpu_vendor'] = cc.cpu_type()
    overall_compute_findings['compute_vt'] = cc.cpu_virt_extensions()
    overall_compute_findings['compute_cores'] = cc.cpu_core_count()
    overall_compute_findings['compute_memory'] = hc.host_memory()
    #pprint.pprint(overall_compute_findings)

    overall_net_findings['nic_quantity'] = nc.nic_count()
    overall_net_findings['nic_type'] = nc.nic_type()
    #pprint.pprint(overall_net_findings)

    overall_storage_findings['storage_attached'] = sc.internal_drive_count()
    overall_storage_findings['storage_controllers'] = sc.get_disk_controllers()
    overall_storage_findings['storage_disks'] = sc.check_disk_size()
    #pprint.pprint(overall_storage_findings)

    host = hc.host_name()
    print "\n\n"
    print "Host Name: %s"%(host['out'])
    #Formatted report ouput to screen
    print 'Overall Host Configuration.'
    print "%-20s %-15s %-15s %-15s"%('Test Ran:','Test Results:','Optional Test:','Test Output:')
    for key,value in overall_host_findings.items():
        if(value['optional'] is False or value['result'] is False):
            print "%-20s %-15s %-15s %-15s" % (value['text'],value['result'],value['optional'],value['out'])

    print "\n\n"
    print 'Host Compute Configuration.'
    print "%-20s %-15s %-15s %-15s"%('Test Ran:','Test Results:','Optional Test:','Test Output:')
    for key,value in overall_compute_findings.items():
            print "%-20s %-15s %-15s %-15s" % (value['text'],value['result'],value['optional'],value['out'])

    print "\n\n"
    print 'Host Network Configuration.'
    print "%-20s %-15s %-15s %-15s"%('Test Ran:','Test Results:','Optional Test:','Test Output:')
    for key,value in overall_net_findings.items():
        if(key == 'nic_type' and len(value['out']) >= 1):
            y=''
            for x in value['out']:
                y += "nic: %s speed: %s brand: %s\n"%(x['nic_name'],x['nic_speed'],x['nic_brand'])
            value['out'] = y
        print "%-20s %-15s %-15s %-15s" % (value['text'],value['result'],value['optional'],value['out'])

    print "\n\n"
    print 'Host Storage Configuration.'
    print "%-20s %-15s %-15s %-15s"%('Test Ran:','Test Results:','Optional Test:','Test Output:')
    for key,value in overall_storage_findings.items():
        if(key == 'storage_disks'):
            y = ''
            for s in value['out']:
                y += "name: %s size: %s valid: %s type: %s\n"%(s['name'],s['size'],s['size_valid'],s['type'])
            value['out'] = y
        if(key == 'storage_controllers'):
            y = ''
            for s in value['out']:
                y += "controller: %s\n"%(s['controller'])
            value['out'] = y
        print "%-20s %-15s %-15s %-15s" % (value['text'],value['result'],value['optional'],value['out'])

elif(proceed.lower == 'n' or proceed.lower == 'no'):
    print "Zerostack pre-flight is exiting, please run the pre-flight checklist before installing the ZCOS on this host(s)"
    exit

else:
    print "Unknown input given."
    exit
