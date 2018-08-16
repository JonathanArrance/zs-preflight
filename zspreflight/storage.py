#!/usr/bin/python
import subprocess

class storage_check():
    def __init__(self):
        self.drives = self._get_drives()
        self.controllers = self._get_storage_controllers()

    def internal_drive_count(self):
        #how many total drives
        ssd = self.drives['ssd_host_disks']
        hdd = self.drives['hdd_host_disks']

        total = ssd + hdd
        out = {'out':ssd + hdd,'result':'Fail','optional':False,'text':'Drive Count'}
        if(total >= 2):
            out = {'out':ssd + hdd,'result':'Pass','optional':False,'text':'Drive Count'}
        return out

    def check_disk_size(self):
        #are the disks in the system the right size
        #out = {'valid':False,'size':0,'name':None}
        drive = []
        for disk in self.drives['disks']:
            size = float(disk['size'][:-1])
            #convert size to MB
            if(disk['size'][-1:] == 'G'):
                size = size * 1000
            elif(disk['size'][-1:] == 'T'):
                size = size * 1000000
            if(size >= 512):
                self.valid_size = 'Pass'
            else:
                self.valid_size = 'Fail'
            disk['size_valid'] = self.valid_size
            drive.append(disk)
        self.drives['out'] = drive
        self.drives['text'] = 'Disk Specs'
        return self.drives

    """
    Coming soon
    def check_disk_controller(self):
        #Are disks attached to a raid controller

        for controller in self.controllers['storage_controllers']
    """

    def get_disk_controllers(self):
        out = {'out':[],'optional':True,'result':'Pass','text':'Storage Controllers'}
        if(len(self.controllers['storage_controllers'])):
            out = {'out':self.controllers['storage_controllers'],'optional':True,'result':'Pass','text':'Storage Controllers'}
        return out

    ###########Internal
    def _get_drives(self):
        try:
            proc = subprocess.Popen("lsblk -d -o name,rota,size | grep -v sr*", stdout=subprocess.PIPE, shell=True)
            (output,err) = proc.communicate()
            output = str(output).strip()
            output = output.split('\n')
            output.pop(0)
            disks = []
            ssd_count = 0
            hdd_count = 0
            out = {'ssd_host_disks':ssd_count,'hdd_host_disks':hdd_count,'disks':disks,'result':False,'optional':False}
            for o in output:
                disk = {}
                split = o.split()
                disk['name'] = split[0]
                if(split[1] == '1'):
                    hdd_count += 1
                    disk['type'] = 'hdd'
                else:
                    ssd_count += 1
                    disk['type'] = 'ssd'
                disk['size'] = split[2]
                disks.append(disk)
            out = {'ssd_host_disks':ssd_count,'hdd_host_disks':hdd_count,'disks':disks,'result':True,'optional':False}
        except Exception as e:
            out = {'ssd_host_disks':None,'hdd_host_disks':None,'disks':None,'result':e,'optional':False}

        return out

    def _get_storage_controllers(self):
        #Get the storage controllers and return them
        try:
            proc = subprocess.Popen("lspci | grep 'IDE\|SATA\|RAID\|SCSI'", stdout=subprocess.PIPE, shell=True)
            (output,err) = proc.communicate()
            output = str(output).strip()
            output = output.split('\n')
            sc_count = len(output)
            controllers = []
            out = {'storage_controller_count':0,'storage_controller_type':controllers,'result':False}
            if(sc_count > 0):
                for o in output:
                    split = o.split(': ')
                    controllers.append({'controller':split[1],'pci':split[0][0:7],'type':split[0][8:]})
                out = {'storage_controller_count':len(controllers),'storage_controllers':controllers,'result':True}
        except Exception as e:
            out = {'storage_controller_count':None,'storage_controllers':[],'result':e}

        return out