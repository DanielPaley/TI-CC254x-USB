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


class HCI_EXT_Events():

    def __init__(self):
        print "Init HCI Ext Events \n"
        self.Commands = {
            'HCI Ext Set Receiver Gain': {'command': 0x04, 'opcode': 0x0400, 'plength': 3,
                                          'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Set Transmitter Power': {'command': 0x04, 'opcode': 0x0401, 'plength': 3,
                                              'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext One Packet Per Event': {'command': 0x04, 'opcode': 0x0402, 'plength': 3,
                                             'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Clock Divide On Halt': {'command': 0x04, 'opcode': 0x0403, 'plength': 3,
                                             'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Declare NV Usage': {'command': 0x04, 'opcode': 0x0404, 'plength': 3,
                                         'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Decrypt': {'command': 0x04, 'opcode': 0x0405, 'plength': 19,
                                'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1], 2: ['plainTextData', byte16]}},

            'HCI Ext Set Local Supported Features': {'command': 0x04, 'opcode': 0x0406, 'plength': 3,
                                                     'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Set Fast Trasmit Response Time': {'command': 0x04, 'opcode': 0x0407, 'plength': 3,
                                                       'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Modem Test Trasmit': {'command': 0x04, 'opcode': 0x0408, 'plength': 3,
                                           'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Modem Hop Test Trasmit': {'command': 0x04, 'opcode': 0x0409, 'plength': 3,
                                               'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Modem Test Receive': {'command': 0x04, 'opcode': 0x040A, 'plength': 3,
                                           'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext End Modem Test': {'command': 0x04, 'opcode': 0x040B, 'plength': 3,
                                       'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Set BDADDR': {'command': 0x04, 'opcode': 0x040C, 'plength': 3,
                                   'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Set SCA': {'command': 0x04, 'opcode': 0x040D, 'plength': 3,
                                'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Set Frequency Tuning': {'command': 0x04, 'opcode': 0x040F, 'plength': 3,
                                             'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Save Frequency Tuning': {'command': 0x04, 'opcode': 0x0410, 'plength': 3,
                                              'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Set Max DTM Transmitter Power': {'command': 0x04, 'opcode': 0x0411, 'plength': 3,
                                                      'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Map PM IO Port': {'command': 0x04, 'opcode': 0x0412, 'plength': 3,
                                       'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Disconnect Immediate': {'command': 0x04, 'opcode': 0x0413, 'plength': 3,
                                             'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Packet error Rate': {'command': 0x04, 'opcode': 0x0414, 'plength': 13,
                                          'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1], 2: ['cmdVal', word1],
                                                        3: ['numPkts', word1], 4: ['numCrcErr', word1], 5: ['numEvents', word1],
                                                        6: ['numMissedEvts', word1]}},

            'HCI Ext Packet Error Rate By Channel': {'command': 0x04, 'opcode': 0x0415, 'plength': 3,
                                                     'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Extend RF Range': {'command': 0x04, 'opcode': 0x0416, 'plength': 3,
                                        'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Halt During RF': {'command': 0x04, 'opcode': 0x0419, 'plength': 3,
                                       'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Set Slave Latency Override': {'command': 0x04, 'opcode': 0x041A, 'plength': 3,
                                                   'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Build Revision': {'command': 0x04, 'opcode': 0x041B, 'plength': 3,
                                       'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1], 3: ['buildRevNum', word1]}},

            'HCI Ext Delay Sleep': {'command': 0x04, 'opcode': 0x041C, 'plength': 3,
                                    'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Reset System': {'command': 0x04, 'opcode': 0x041D, 'plength': 3,
                                     'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Overlapped Processing': {'command': 0x04, 'opcode': 0x041E, 'plength': 3,
                                              'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

            'HCI Ext Number Completed Packets Limit': {'command': 0x04, 'opcode': 0x041F, 'plength': 3,
                                                       'parameter': {0: ['Status', byte1], 1: ['cmdOpcode', word1]}},

        }

        self.Opcode_Lookup = {
            0x0400: 'HCI Ext Set Receiver Gain',
            0x0401: 'HCI Ext Set Transmitter Power',
            0x0402: 'HCI Ext One Packet Per Event',
            0x0403: 'HCI Ext Clock Divide On Halt',
            0x0404: 'HCI Ext Declare NV Usage',
            0x0405: 'HCI Ext Decrypt',
            0x0406: 'HCI Ext Set Local Supported Features',
            0x0407: 'HCI Ext Set Fast Trasmit Response Time',
            0x0408: 'HCI Ext Modem Test Trasmit',
            0x0409: 'HCI Ext Modem Hop Test Trasmit',
            0x040A: 'HCI Ext Modem Test Receive',
            0x040B: 'HCI Ext End Modem Test',
            0x040C: 'HCI Ext Set BDADDR',
            0x040D: 'HCI Ext Set SCA',
            0x040F: 'HCI Ext Set Frequency Tuning',
            0x0410: 'HCI Ext Save Frequency Tuning',
            0x0411: 'HCI Ext Set Max DTM Transmitter Power',
            0x0412: 'HCI Ext Map PM IO Port',
            0x0413: 'HCI Ext Disconnect Immediate',
            0x0414: 'HCI Ext Packet error Rate',
            0x0415: 'HCI Ext Packet Error Rate By Channel',
            0x0416: 'HCI Ext Extend RF Range',
            0x0419: 'HCI Ext Halt During RF',
            0x041A: 'HCI Ext Set Slave Latency Override',
            0x041B: 'HCI Ext Build Revision',
            0x041C: 'HCI Ext Delay Sleep',
            0x041D: 'HCI Ext Reset System',
            0x041E: 'HCI Ext Overlapped Processing',
            0x041F: 'HCI Ext Number Completed Packets Limit',
        }

        self.ops = CmdEvtOps(self.Commands, self.Opcode_Lookup)

    def Event_Lookup(self, item):
        return self.ops.Event_Lookup(item)

    def Create_Packet(self, cmd, **Parameter):
        return self.ops.Create_Command_Packet(cmd, **Parameter)

    def Decode_Packet(self, event, packet):
        self.ops.Decode_Packet(event, packet)


if __name__ == '__main__':
    a = HCI_EXT_Events()
    a.Create_Packet('HCI Ext Set Receiver Gain', Status=0x00, cmdOpcode=0xFC00)

   # a.Create_Command_Packet('HCI Ext Decrypt',key='0x1102030405060708090a0b0c0d0e00f', \
#                                encText='0x12030405060708090a0b0c0d0e0f1')
    a.Decode_Packet(0x040A, [0x00, 0x01])
