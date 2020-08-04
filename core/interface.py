# Date: 04/08/2020
# Distro: Kali linux
# Author: MR.CRACKED
# Description: Interface handler

from os import devnull
from subprocess import Popen
from core.mac import Generator as macGen

class Interface(object):
 def __init__(self,iface):
  self.wlan = iface
  self.devnull  = open(devnull,'w')
  self.mac = macGen().generate()

 def managedMode(self):
  self.destroyInterface()
  cmd = 'service network-manager restart'
  Popen(cmd,stdout=self.devnull,stderr=self.devnull,shell=True).wait()

 def changeMac(self):
  cmd ='ifconfig mon0 down && iwconfig mon0 mode monitor &&\
        macchanger -m {} mon0 && service\
        network-manager stop && ifconfig mon0 up'.format(self.mac)

  Popen(cmd,stdout=self.devnull,stderr=self.devnull,shell=True).wait()

 def monitorMode(self):
  self.destroyInterface()
  Popen('iw {} interface add mon0 type monitor'.format(self.wlan),
  stdout=self.devnull,stderr=self.devnull,shell=True).wait()
  self.changeMac()

 def destroyInterface(self):
  Popen('iw dev mon0 del',stdout=self.devnull,
  stderr=self.devnull,shell=True).wait()
