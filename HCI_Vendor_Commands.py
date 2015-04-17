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



from dataMaster import *
from CmdEvtOps import *


class HCI_Vendor_Commands():

    def __init__(self):
        print "Init Command Format"
        self.Commands = {
            'HCI_ReadRSSI': {'command': 0x01, 'opcode': 0x1405, 'plength': 2,
                             'parameter': {0: ['connHandle', word1]}},

            'HCI_LEClearWhiteList': {'command': 0x01, 'opcode': 0x2010, 'plength': 0,
                                     'parameter': {}},

            'HCI_LEAddDeviceToWhiteList': {'command': 0x01, 'opcode': 0x2011, 'plength': 7,
                                           'parameter': {0: ['addrType', byte1], 1: ['devAddr', byte6]}},

            'HCI_LERemoveDeviceFromWhiteList': {'command': 0x01, 'opcode': 0x2012, 'plength': 7,
                                                'parameter': {0: ['addrType', byte1], 1: ['devAddr', byte6]}},

            'HCI_LEConnectionUpdate': {'command': 0x01, 'opcode': 0x2013, 'plength': 14,
                                       'parameter': {0: ['handle', word1], 1: ['connInterval', word1], 
                                                     2: ['connIntervalMax', word1], 3: ['connLatency', byte2],
                                                     4: ['connTimeout', word1], 5: ['minimumLength', word1], 
                                                     6: ['maximumLength', word1]}}
        }
        self.Opcode_Lookup = {
            0x1405: 'HCI_ReadRSSI',
            0x2010: 'HCI_LEClearWhiteList',
            0x2011: 'HCI_LEAddDeviceToWhiteList',
            0x2012: 'HCI_LERemoveDeviceFromWhiteList',
            0x2013: 'HCI_LEConnectionUpdate',
        }

        self.ops = CmdEvtOps(self.Commands, self.Opcode_Lookup)

    def Event_Lookup(self, item):
        return self.ops.Event_Lookup(item)

    def Create_Packet(self, cmd, **Parameter):
        return self.ops.Create_Command_Packet(cmd, **Parameter)

    def Decode_Packet(self, event, packet):
        self.ops.Decode_Packet(event, packet)


if __name__ == '__main__':
    a = HCI_Vendor_Commands()
    a.Create_Packet('HCI_LEClearWhiteList')
