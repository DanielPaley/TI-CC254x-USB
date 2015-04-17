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


class Other_Vendor_Commands():

    def __init__(self):
        print "Init Command Format"
        self.Commands = {
            'UTIL_Reset': {'command': 0x01, 'opcode': 0xFE80, 'plength': 0,
                           'parameter': {}},

            'UTIL_NVRead': {'command': 0x01, 'opcode': 0xFE81, 'plength': 2,
                            'parameter': {0: ['nvID', byte1], 1: ['nvDataLen', byte1]}},

            'UTIL_NVWrite': {'command': 0x01, 'opcode': 0xFE82, 'plength': 2,
                             'parameter': {0: ['nvID', byte1], 1: ['nvDataLen', byte1], 
                                           2: ['nvData', Nbyte]}},

            'UTIL_ForceBoot': {'command': 0x01, 'opcode': 0xFE83, 'plength': 0,
                               'parameter': {}},

            'L2CAP_InfoReq': {'command': 0x01, 'opcode': 0xFC8A, 'plength': 4,
                              'parameter': {0: ['connHandle', word1], 1: ['infoType', word1]}},

            'L2CAP_ConnParamUpdateReq': {'command': 0x01, 'opcode': 0xFC92, 'plength': 10,
                                         'parameter': {0: ['connHandle', word1], 1: ['intervalMin', word1],
                                                       2: ['intervalMax', word1], 3: ['slaveLatency', word1], 
                                                       4: ['tineoutMultiplier', word1]}}
        }

        self.Opcode_Lookup = {
            0xFE80: 'UTIL_Reset',
            0xFE81: 'UTIL_NVRead',
            0xFE82: 'UTIL_NVWrite',
            0xFE83: 'UTIL_ForceBoot',
            0xFC8A: 'L2CAP_InfoReq',
            0xFC92: 'L2CAP_ConnParamUpdateReq',
        }

        self.ops = CmdEvtOps(self.Commands, self.Opcode_Lookup)

    def Event_Lookup(self, item):
        return self.ops.Event_Lookup(item)

    def Create_Packet(self, cmd, **Parameter):
        return self.ops.Create_Command_Packet(cmd, **Parameter)

    def Decode_Packet(self, event, packet):
        self.ops.Decode_Packet(event, packet)


if __name__ == '__main__':
    a = Other_Vendor_Commands()
    a.Create_Packet('UTIL_Reset')
