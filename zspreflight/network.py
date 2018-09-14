#!/usr/bin/python
import subprocess

class network_check():
    def __init__(self):
        pass

    def nic_count(self):
        out = {'out':0,'result':'Fail','optional':False,'text':'System NIC Count'}
        try:
            proc = subprocess.Popen("ls -I br* -I lo -I vir* /sys/class/net/", stdout=subprocess.PIPE, shell=True)
            (output,err) = proc.communicate()
            output = str(output).strip()
            output = len(output.split('\n'))
            out = {'out':output,'result':'Pass','optional':False,'text':'System NIC Count'}
        except Exception as e:
            out = {'out':'Unknown','result':e,'optional':False,'text':'System NIC Count'}

        return out

    def nic_type(self):
        #nic speed
        #nic type
        nic = []
        out = {'result':'Fail','optional':False,'out':nic,'text':'System Nic Info'}
        try:
            proc = subprocess.Popen("ls -I br* -I lo -I vir* /sys/class/net/", stdout=subprocess.PIPE, shell=True)
            (output,err) = proc.communicate()
            output = str(output).strip()
            output = output.split('\n')
            for o in output:
                did = subprocess.Popen("ls -al /sys/class/net/%s/device"%o, stdout=subprocess.PIPE, shell=True)
                (didout,err) = did.communicate()
                didout = str(didout).strip()[-7:]
                #use lspci and grep to get nicbrand
                brand = subprocess.Popen("lspci | grep %s"%didout, stdout=subprocess.PIPE, shell=True)
                (brandout,err) = brand.communicate()
                nic_brand = str(brandout).strip()[29:]
                if(nic_brand == ''):
                    nic_brand = 'Unknown'
                try:
                    speed = open("/sys/class/net/%s/speed"%o,'r')
                    print speed.read()
                    nic_speed = 0
                    if(int(speed.read().strip()) > 0):
                        nic_speed = int(speed.read().strip())
                        if(nic_speed == 1000):
                            nic.append({'nic_name':o,'nic_speed':nic_speed,'nic_brand':nic_brand,'text':'NIC minimum config'})
                        elif(nic_speed >= 10000):
                            nic.append({'nic_name':o,'nic_speed':nic_speed,'nic_brand':nic_brand,'text':'NIC recommended config'})
                except Exception as e:
                    nic.append({'nic_name':o,'nic_speed':'Unknown','nic_brand':nic_brand,'text':'NIC Unknown'})
            out = {'result':'Pass','optional':False,'out':nic,'text':'System Nic Info'}
        except Exception as e:
            out = {'result':e,'optional':False,'out':nic,'text':'System Nic Info'}

        return out

    """
    def nic_lacp_network(self):
        #comeing soon
        #is LACP enabled on the NIC

        pass
    """
