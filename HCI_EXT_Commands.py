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


class HCI_EXT_Commands():

    def __init__(self):
        print "Init Command Format"
        self.Commands = {
            'HCI Ext Set Receiver Gain': {'command': 0x01, 'opcode': 0xFC00, 'plength': 1,
                                          'parameter': {0: ['rxGain', byte1]}},

            'HCI Ext Set Transmitter Power': {'command': 0x01, 'opcode': 0xFC01, 'plength': 1,
                                              'parameter': {0: ['txPower', byte1]}},

            'HCI Ext One Packet Per Event': {'command': 0x01, 'opcode': 0xFC02, 'plength': 1,
                                             'parameter': {0: ['control', byte1]}},

            'HCI Ext Clock Divide On Halt': {'command': 0x01, 'opcode': 0xFC03, 'plength': 1,
                                             'parameter': {0: ['control', byte1]}},

            'HCI Ext Declare NV Usage': {'command': 0x01, 'opcode': 0xFC04, 'plength': 1,
                                         'parameter': {0: ['mode', byte1]}},

            'HCI Ext Decrypt': {'command': 0x01, 'opcode': 0xFC05, 'plength': 16,
                                'parameter': {0: ['key', word4], 1: ['encText', word4]}},

            'HCI Ext Set Local Supported Features': {'command': 0x01, 'opcode': 0xFC06, 'plength': 8,
                                                     'parameter': {0: ['localFeatures', word4]}},

            'HCI Ext Set Fast Trasmit Response Time': {'command': 0x01, 'opcode': 0xFC07, 'plength': 1,
                                                       'parameter': {0: ['control', byte1]}},

            'HCI Ext Modem Test Trasmit': {'command': 0x01, 'opcode': 0xFC08, 'plength': 2,
                                           'parameter': {0: ['cwMode', byte1], 1: ['txFreq', byte1]}},

            'HCI Ext Modem Hop Test Trasmit': {'command': 0x01, 'opcode': 0xFC09, 'plength': 0,
                                               'parameter': {}},

            'HCI Ext Modem Test Receive': {'command': 0x01, 'opcode': 0xFC0A, 'plength': 1,
                                           'parameter': {0: ['rxFreq', byte1]}},

            'HCI Ext End Modem Test': {'command': 0x01, 'opcode': 0xFC0B, 'plength': 0,
                                       'parameter': {}},

            'HCI Ext Set BDADDR': {'command': 0x01, 'opcode': 0xFC0C, 'plength': 6,
                                   'parameter': {0: ['bdAddr', word3]}},

            'HCI Ext Set SCA': {'command': 0x01, 'opcode': 0xFC0D, 'plength': 2,
                                'parameter': {0: ['scaInPPM', word1]}},

            'HCI Ext Enable PTM': {'command': 0x01, 'opcode': 0xFC0E, 'plength': 0,
                                   'parameter': {}},

            'HCI Ext Set Frequency Tuning': {'command': 0x01, 'opcode': 0xFC0F, 'plength': 1,
                                             'parameter': {0: ['step', byte1]}},

            'HCI Ext Save Frequency Tuning': {'command': 0x01, 'opcode': 0xFC10, 'plength': 0,
                                              'parameter': {}},

            'HCI Ext Set Max DTM Transmitter Power': {'command': 0x01, 'opcode': 0xFC11, 'plength': 1,
                                                      'parameter': {0: ['txPower', byte1]}},

            'HCI Ext Map PM IO Port': {'command': 0x01, 'opcode': 0xFC12, 'plength': 2,
                                       'parameter': {0: ['ioPort', byte1], 1: ['ioPin', byte1]}},

            'HCI Ext Disconnect Immediate': {'command': 0x01, 'opcode': 0xFC13, 'plength': 2,
                                             'parameter': {0: ['connHandle', word1]}},

            'HCI Ext Packet error Rate': {'command': 0x01, 'opcode': 0xFC14, 'plength': 3,
                                          'parameter': {0: ['connHandle', word1], 1: ['command', byte1]}},

            'HCI Ext Packet Error Rate By Channel': {'command': 0x01, 'opcode': 0xFC15, 'plength': 3,
                                                     'parameter': {0: ['connHandle', word1], 1: ['perByChan', byte1]}},

            'HCI Ext Extend RF Range': {'command': 0x01, 'opcode': 0xFC16, 'plength': 0,
                                        'parameter': {}},

            'HCI Ext Advertiser Event Notice': {'command': 0x01, 'opcode': 0xFC17, 'plength': 3,
                                                'parameter': {0: ['taskID', byte1], 1: ['taskEvent', word1]}},

            'HCI Ext Connection Event Notice': {'command': 0x01, 'opcode': 0xFC18, 'plength': 3,
                                                'parameter': {0: ['taskID', byte1], 1: ['taskEvent', word1]}},

            'HCI Ext Halt During RF': {'command': 0x01, 'opcode': 0xFC19, 'plength': 1,
                                       'parameter': {0: ['mode', byte1]}},

            'HCI Ext Set Slave Latency Override': {'command': 0x01, 'opcode': 0xFC1A, 'plength': 1,
                                                   'parameter': {0: ['mode', byte1]}},

            'HCI Ext Build Revision': {'command': 0x01, 'opcode': 0xFC1B, 'plength': 3,
                                       'parameter': {0: ['mode', byte1], 1: ['userRevNum', word1]}},

            'HCI Ext Delay Sleep': {'command': 0x01, 'opcode': 0xFC1C, 'plength': 2,
                                    'parameter': {0: ['delay', word1]}},

            'HCI Ext Reset System': {'command': 0x01, 'opcode': 0xFC1D, 'plength': 1,
                                     'parameter': {0: ['mode', byte1]}},

            'HCI Ext Overlapped Processing': {'command': 0x01, 'opcode': 0xFC1E, 'plength': 1,
                                              'parameter': {0: ['mode', byte1]}},

            'HCI Ext Number Completed Packets Limit': {'command': 0x01, 'opcode': 0xFC1F, 'plength': 2,
                                                       'parameter': {0: ['limit', byte1], 1: ['flushOnEvt', byte1]}}
        }

        self.Opcode_Lookup = {
            0xFC00: 'HCI Ext Set Receiver Gain',
            0xFC01: 'HCI Ext Set Transmitter Power',
            0xFC02: 'HCI Ext One Packet Per Event',
            0xFC03: 'HCI Ext Clock Divide On Halt',
            0xFC04: 'HCI Ext Declare NV Usage',
            0xFC05: 'HCI Ext Decrypt',
            0xFC06: 'HCI Ext Set Local Supported Features',
            0xFC07: 'HCI Ext Set Fast Trasmit Response Time',
            0xFC08: 'HCI Ext Modem Test Trasmit',
            0xFC09: 'HCI Ext Modem Hop Test Trasmit',
            0xFC0A: 'HCI Ext Modem Test Receive',
            0xFC0B: 'HCI Ext End Modem Test',
            0xFC0C: 'HCI Ext Set BDADDR',
            0xFC0D: 'HCI Ext Set SCA',
            0xFC0E: 'HCI Ext Enable PTM',
            0xFC0F: 'HCI Ext Set Frequency Tuning',
            0xFC10: 'HCI Ext Save Frequency Tuning',
            0xFC11: 'HCI Ext Set Max DTM Transmitter Power',
            0xFC12: 'HCI Ext Map PM IO Port',
            0xFC13: 'HCI Ext Disconnect Immediate',
            0xFC14: 'HCI Ext Packet error Rate',
            0xFC15: 'HCI Ext Packet Error Rate By Channel',
            0xFC16: 'HCI Ext Extend RF Range',
            0xFC17: 'HCI Ext Advertiser Event Notice',
            0xFC18: 'HCI Ext Connection Event Notice',
            0xFC19: 'HCI Ext Halt During RF',
            0xFC1A: 'HCI Ext Set Slave Latency Override',
            0xFC1B: 'HCI Ext Build Revision',
            0xFC1C: 'HCI Ext Delay Sleep',
            0xFC1D: 'HCI Ext Reset System',
            0xFC1E: 'HCI Ext Overlapped Processing',
            0xFC1F: 'HCI Ext Number Completed Packets Limit'
        }

        self.ops = CmdEvtOps(self.Commands, self.Opcode_Lookup)

    def Event_Lookup(self, item):
        return self.ops.Event_Lookup(item)

    def Create_Packet(self, cmd, **Parameter):
        return self.ops.Create_Command_Packet(cmd, **Parameter)

    def Decode_Packet(self, event, packet):
        self.ops.Decode_Packet(event, packet)


if __name__ == '__main__':
    a = HCI_EXT_Commands()
    a.Create_Packet('HCI Ext Set Receiver Gain', rxGain=0x00)

    a.Create_Packet('HCI Ext Decrypt', key='0x1102030405060708090a0b0c0d0e00f',
                    encText='0x12030405060708090a0b0c0d0e0f1')
