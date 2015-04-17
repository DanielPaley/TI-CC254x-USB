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


class GAP_Vendor_Commands():

    def __init__(self):
        print "Init GAP Commands"
        self.Command = {
            'GAP Device Initialization': {'command': 0x01, 'opcode': 0xFE00, 'plength': 36,
                                          'parameter': {0: ['profileRole', byte1], 1: ['maxScanResponses', byte1], 2: ['IRK', byte16],
                                                        3: ['CSRK', byte16], 4: ['signCounter', word2]}},

            'GAP Configure Device Address': {'command': 0x01, 'opcode': 0x0FE03, 'plength': 7,
                                             'parameter': {0: ['addrType', byte1], 1: ['Addr', byte6]}},

            'GAP Device Discovery Request': {'command': 0x01, 'opcode': 0x0FE04, 'plength': 3,
                                             'parameter': {0: ['mode', byte1], 1: ['activeScan', byte1], 2: ['whiteList', byte1]}},

            'GAP Device Discovery Cancel': {'command': 0x01, 'opcode': 0xFE05, 'plength': 0,
                                            'parameter': {}},

            'GAP Make Discoverable': {'command': 0x01, 'opcode': 0xFE06, 'plength': 10,
                                      'parameter': {0: ['eventType', byte1], 1: ['initiatorAddrType', byte1], 2: ['initiatorAddr', byte6],
                                                    3: ['channelMap', byte1], 4: ['filterPolicy', byte1]}},

            'GAP Update Advertising Data': {'command': 0x01, 'opcode': 0xFE07, 'plength': 2,
                                            'parameter': {0: ['adType', byte1], 1: ['dataLen', byte1], 2: ['advertData', Nbyte]}},

            'GAP End Discoverable': {'command': 0x01, 'opcode': 0xFE08, 'plength': 0,
                                     'parameter': {}},

            'GAP Establish Link Request': {'command': 0x01, 'opcode': 0xFE09, 'plength': 9,
                                           'parameter': {0: ['highDutyCycle', byte1], 1: ['whiteList', byte1], 
                                                         2: ['addrTypePeer', byte1], 3: ['peerAddr', byte6]}},

            'GAP Terminate Link Request': {'command': 0x01, 'opcode': 0xFE0A, 'plength': 2,
                                           'parameter': {0: ['connHandle', word1]}},

            'GAP Authenticate': {'command': 0x01, 'opcode': 0xFE0B, 'plength': 29,
                                 'parameter': {0: ['connHandle', word1], 1: ['secReq.ioCaps', byte1], 2: ['secReq.oobAvailable', byte1],
                                               3: ['secReq.oob', byte16], 4: ['secReq.authReq', byte1], 5: ['secReq.maxEncKeySize', byte1],
                                               6: ['secReq.keyDist', byte1], 7: ['pairReq.Enable', byte1], 8: ['pairReq.ioCaps', byte1],
                                               9: ['pairReq.oobDataFlag', byte1], 10: ['pairReq.authReq', byte1], 
                                               11: ['pairReq.maxEncKeySize', byte1], 12: ['pairReq.keyDist', byte1]}},

            'GAP Update Link Parameter Request': {'command': 0x01, 'opcode': 0xFE11, 'plength': 10,
                                                  'parameter': {0: ['connectionHandle', word1], 1: ['intervalMin', word1], 
                                                                2: ['intervalMax', word1], 3: ['connLatency', word1], 
                                                                4: ['connTimeout', word1]}},

            'GAP Passkey Update': {'command': 0x01, 'opcode': 0xFE0C, 'plength': 8,
                                   'parameter': {0: ['connHandle', word1], 1: ['passkey', byte6]}},

            'GAP Slave Security Request': {'command': 0x01, 'opcode': 0xFE0D, 'plength': 3,
                                           'parameter': {0: ['connHandle', word1], 1: ['authReq', byte1]}},

            'GAP Signable': {'command': 0x01, 'opcode': 0xFE0E, 'plength': 21,
                             'parameter': {0: ['connHandle', word1], 1: ['authenticated', byte1], 2: ['CSRK', byte16], 
                                           3: ['signCounter', word2]}},

            'GAP Bond': {'command': 0x01, 'opcode': 0xFE0F, 'plength': 30,
                         'parameter': {0: ['connHandle', word1], 1: ['authenticated', byte1], 2: ['LTK', byte16], 
                                       3: ['DVI', word1], 4: ['rand', byte8], 5: ['LTKsize', byte1]}},

            'GAP Terminate Auth': {'command': 0x01, 'opcode': 0xFE10, 'plength': 3,
                                   'parameter': {0: ['connHandle', word1], 1: ['reason', byte1]}},

            'GAP Set Parameter': {'command': 0x01, 'opcode': 0xFE30, 'plength': 3,
                                  'parameter': {0: ['paramID', byte1], 1: ['paramValue', word1]}},

            'GAP Get Parameter': {'command': 0x01, 'opcode': 0xFE31, 'plength': 1,
                                  'parameter': {0: ['paramID', byte1]}},

            'GAP Resolve Private Address': {'command': 0x01, 'opcode': 0xFE32, 'plength': 22,
                                            'parameter': {0: ['IRK', byte16], 1: ['addr', byte6]}},

            'GAP Set Advertisement Token': {'command': 0x01, 'opcode': 0xFE33, 'plength': 2,
                                            'parameter': {0: ['adType', byte1], 1: ['advDataLen', byte1], 2: ['advData', Nbyte]}},

            'GAP Remove Advertisement Token': {'command': 0x01, 'opcode': 0xFE34, 'plength': 1,
                                               'parameter': {0: ['adType', byte1]}},

            'GAP Update Advertisement Tokens': {'command': 0x01, 'opcode': 0xFE35, 'plength': 0,
                                                'parameter': {}},

            'GAP Bond Set Parameter': {'command': 0x01, 'opcode': 0xFE36, 'plength': 3,
                                       'parameter': {0: ['paramID', word1], 1: ['paramDataLen', byte1], 2: ['paramData', Nbyte]}},

            'GAP Bond Get Parameter': {'command': 0x01, 'opcode': 0xFE37, 'plength': 2,
                                       'parameter': {0: ['paramID', word1]}}
        }

        self.Opcode_Lookup = {
            0xFE00: 'GAP Device Initialization',
            0x0FE03: 'GAP Configure Device Address',
            0x0FE04: 'GAP Device Discovery Request',
            0xFE05: 'GAP Device Discovery Cancel',
            0xFE06: 'GAP Make Discoverable',
            0xFE07: 'GAP Update Advertising Data',
            0xFE08: 'GAP End Discoverable',
            0xFE09: 'GAP Establish Link Request',
            0xFE0A: 'GAP Terminate Link Request',
            0xFE0B: 'GAP Authenticate',
            0xFE11: 'GAP Update Link Parameter Request',
            0xFE0C: 'GAP Passkey Update',
            0xFE0D: 'GAP Slave Security Request',
            0xFE0E: 'GAP Signable',
            0xFE0F: 'GAP Bond',
            0xFE10: 'GAP Terminate Auth',
            0xFE30: 'GAP Set Parameter',
            0xFE31: 'GAP Get Parameter',
            0xFE32: 'GAP Resolve Private Address',
            0xFE33: 'GAP Set Advertisement Token',
            0xFE34: 'GAP Remove Advertisement Token',
            0xFE35: 'GAP Update Advertisement Tokens',
            0xFE36: 'GAP Bond Set Parameter',
            0xFE37: 'GAP Bond Get Parameter'
        }

        self.ops = CmdEvtOps(self.Command, self.Opcode_Lookup)

    def Event_Lookup(self, item):
        return self.ops.Event_Lookup(item)

    def Create_Packet(self, cmd, **Parameter):

        a = self.ops.Create_Command_Packet(cmd, **Parameter)
        return a

    def Decode_Packet(self, event, packet):
        self.ops.Decode_Packet(event, packet)


if __name__ == '__main__':
    print "Main:"
    a = GAP_Vendor_Commands()
    a.Create_Packet(
        'GAP Device Discovery Request', mode=0x00, activeScan=0x00, whiteList=0x00)
    a.Create_Packet('GAP End Discoverable')
