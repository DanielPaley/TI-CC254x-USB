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
import os
import sys
import time
from threading import Thread

from ATT_Vendor_Commands import *
from GAP_Vendor_Commands import *
from GAP_Vendor_Events import *
from GATT_Vendor_Commands import *

from HCI_EXT_Commands import *
from HCI_EXT_Events import *
from HCI_Vendor_Commands import *

from Other_Vendor_Commands import *
from Return_Handler import *
from inputKey import *


def initserial():
    ''' GAP Device Initialization
           Packet is as follow:
           - packet type (1 byte)
           - GAP command (2 bytes)
           - length of data (1 byte)
           - Data:
               i)   GAP Profile Role (1 byte) (Central)
              ii)  Maximum Scan Responses to accept (1 byte) (0x00-0xFF)
             iii) IRK (16 bytes) if all zeros, randomly generated
              iv)  CSRK (16 bytes) if all zeros, randomly generated
               v)   Signature counter initial value (4 bytes)
    '''

    bt = serial.Serial()
    if os.name == 'posix':
        bt.port = "/dev/ttyACM0"
    else:
        bt.port = "COM3"
    bt.baudrate = 57600
    bt.baudrate = 115200
    bt.stopbits = 1
    bt.parity = 'N'
    bt.bytesize = 8
    bt.xonxoff = 0
    bt.rtscts = 1
    bt.timeout = 0
    bt.open()
    return bt



bt = initserial()
print("Connected to Dongle")


print("Starting Threads")
# startup threads
writeThread = inputKey(bt)
readThread = Return_Handler(bt)

writeThread.start()
readThread.start()


while(bt.isOpen()):  # Read a new packet
    time.sleep(1)
