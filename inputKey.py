#-----------------------------------------------------------------------------------
#Copyright (c) 2015 Lab Sensor Solutions, Inc.
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#-----------------------------------------------------------------------------------
#
# Author: D.Paley
# Date:   4/3/2015
# Release: ALPHA
#
#-----------------------------------------------------------------------------------
#

import serial
import struct
import time
import os
import sys
from threading import Thread

from dataMaster import *
from CmdEvtOps import *


from GAP_Vendor_Commands import *
from GAP_Vendor_Events import *
from HCI_EXT_Commands import *
from HCI_EXT_Events import *
from Other_Vendor_Commands import *
from Return_Handler import *


class inputKey(Thread):
    Device = None
    GVC = None

    def __init__(self, BTDongle=None):
        # GAP Device Initialization
        #
        # Packet is as follow:
        #	- packet type (1 byte)
        #	- GAP command (2 bytes)
        #	- length of data (1 byte)
        #	- Data:
        #		i)   GAP Profile Role (1 byte) (Central)
        #		ii)  Maximum Scan Responses to accept (1 byte) (0x00-0xFF)
        #		iii) IRK (16 bytes) if all zeros, randomly generated
        #		iv)  CSRK (16 bytes) if all zeros, randomly generated
        #		v)   Signature counter initial value (4 bytes)

        Thread.__init__(self)
        self.GVC = GAP_Vendor_Commands()
        inputKey.Device = BTDongle
        print 'Initialized inputKey'
        inputKey.Device.write(self.GVC.Create_Packet('GAP Device Initialization', profileRole=0x08, maxScanResponses=0x03,
                                                     IRK='0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00',
                                                     CSRK='0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00:0x00',
                                                     signCounter=0x01))

    def run(self):
        while inputKey.Device.isOpen():
            count = inputKey.Device.inWaiting()
            ouut = '?[%d]:' % count
            keyin = raw_input(ouut)
            print "[" + keyin + ']\n'

            if keyin == "d":
                inputKey.Device.write(self.GVC.Create_Packet('GAP Device Discovery Request', mode=0x03, activeScan=0x01, whiteList=0x00))
            elif keyin == 'c':
                inputKey.Device.write(
                    self.GVC.Create_Packet('GAP Device Discovery Cancel'))
            elif keyin == 'q':
                inputKey.Device.close()
            elif keyin == 'i':
                inputKey.Device.write(self.GVC.Create_Packet('GAP Device Initialization', profileRole=0x08, maxScanResponses=0x03,
                                                             IRK=0x00, CSRK=0x00, signCounter=0x01))
            elif keyin == 'f':
                inputKey.Device.flushOutput()
                inputKey.Device.flushInput()
