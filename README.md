# zs-preflight
A preflight checklist script that will help an admin determine if the hardware they want to use for Zerostack is compatible.

This is an automated preflight checklist that will work on a base ubuntu OS (14.04,16.04), and requires a minimum of python 2.7.

The preflight check will ensure that your physical server will work with the Zerostack ZCOS. Once this script is run, and
all of the checks are varified, you will be able to install the ZCOS.

The preflight check will make sure the following adhears to the Zerostack minimal viable hardware spec.

1. Overall system configuration
2. CPU architecture
3. Storage requierments
4. Networking

Please check the Ubuntu HCL to verify your results.
[Ubuntu Server HCL](https://certification.ubuntu.com/server/)

Once all of the results have been verified, please send your output file to support@zerostack.com

## Install
### GIT - development / nightly
* git clone https://github.com/JonathanArrance/zsdev.git
* cd zspreflight
* python setup.py

### PIP - test build

  python -m pip install --index-url https://test.pypi.org/simple/ zspreflight

### PIP - stable build

  pip install zspreflight

### Operation

  $ python ~/.local/lib/python2.7/site-packages/zspreflight/preflight.py
  
### Sample Run
[admin@nfs zspreflight]# python preflight.py
Zerostack pre-flight check system.
Do you want to proceed? (yes/no)yes



Host Name: nfs


Overall Host Configuration.
Test Ran:            Test Results:   Optional Test:  Test Output:   
CPU Architecture     Pass            False           x86_64         
CPU Not Virtualized  Pass            False           None           
System NIC Count     Pass            False           6              
Drive Count          Pass            False           12             
Host USB2 Ports      Pass            False           1              



Host Compute Configuration.
Test Ran:            Test Results:   Optional Test:  Test Output:   
Host Memory          Pass            False           126GB - recommended amount of memory
Virtual extensions   Pass            False           AMD-V          
CPU Vendor           Pass            False           AuthenticAMD   
Physical cores       Pass            False           16             
CPU Architecture     Pass            False           x86_64         



Host Network Configuration.
Test Ran:            Test Results:   Optional Test:  Test Output:   
System NIC Count     Pass            False           6              



Host Storage Configuration.
Test Ran:            Test Results:   Optional Test:  Test Output:   
Drive Count          Pass            False           12             



Discovered Hardware.


NICS Discovered.
NIC:                 Speed:          Brand:          Output:        
eth0                 Unknown         Intel Corporation Ethernet Controller 10-Gigabit X540-AT2 (rev 01) NIC Unknown    
eth1                 Unknown         Intel Corporation Ethernet Controller 10-Gigabit X540-AT2 (rev 01) NIC Unknown    
eth2                 Unknown         Intel Corporation 82574L Gigabit Network Connection NIC Unknown    
eth3                 Unknown         Intel Corporation 82574L Gigabit Network Connection NIC Unknown    
eth4                 Unknown         3Com Corporation 3c905C-TX/TX-M [Tornado] (rev 30) NIC Unknown    
eth5                 Unknown         ADMtek NC100 Network Everywhere Fast Ethernet 10/100 (rev 11) NIC Unknown    


Disks Discovered.
Drive Name:          Drive Size:     Drive Valid:    Drive Type:    
sdc                  2.7T            Pass            hdd            
sda                  111.8G          Pass            ssd            
sdb                  111.8G          Pass            ssd            
sdd                  2.7T            Pass            hdd            
sdf                  2.7T            Pass            hdd            
sde                  2.7T            Pass            hdd            
sdg                  2.7T            Pass            hdd            
sdi                  2.7T            Pass            hdd            
sdh                  2.7T            Pass            hdd            
sdj                  2.7T            Pass            hdd            
sdk                  2.7T            Pass            hdd            
sdl                  2.7T            Pass            hdd            


RAID Controllers Discovered.
Storage Controller:                                          PCI Interface:            Controller Type:         
Advanced Micro Devices, Inc. [AMD/ATI] SB7x0/SB8x0/SB9x0 SATA Controller [AHCI mode] 00:11.0                   SATA controller          
Silicon Image, Inc. SiI 3124 PCI-X Serial ATA Controller (rev 02) 03:04.0                   RAID bus controller      
Silicon Image, Inc. SiI 3124 PCI-X Serial ATA Controller (rev 02) 05:04.0                   RAID bus controller
