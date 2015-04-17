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


class GAP_Vendor_Events():

    def __init__(self):
        print "Init GAP Events"
        self.Commands = {
            'GAP Device Init Done': {'command': 0x04, 'opcode': 0x0600, 'plength': 42,
                                     'parameter': {0: ['Status', byte1], 1: ['devAddr', byte6], 2: ['dataPktLen', word1],
                                                   3: ['numDataPkts', byte1], 4: ['IRK', byte16], 5: ['CSRK', byte16]}},

            'GAP Device Discovery': {'command': 0x04, 'opcode': 0x0601, 'plength': 2,
                                     'parameter': {0: ['Status', byte1], 1: ['numDevs', byte1], 
                                                   2: ['array', N1byte1byte6byte]}},

            'GAP Advert Data Update Done': {'command': 0x04, 'opcode': 0x0602, 'plength': 2,
                                            'parameter': {0: ['Status', byte1], 1: ['adType', byte1]}},

            'GAP Make Discoverable Done': {'command': 0x04, 'opcode': 0x0603, 'plength': 1,
                                           'parameter': {0: ['Status', byte1]}},

            'GAP End Discoverable Done': {'command': 0x04, 'opcode': 0x0604, 'plength': 1,
                                          'parameter': {0: ['Status', byte1]}},

            'GAP Link Established': {'command': 0x04, 'opcode': 0x0605, 'plength': 17,
                                     'parameter': {0: ['Status', byte1], 1: ['devAddrType', byte1], 
                                                   2: ['devAddr', byte6], 3: ['connHandle', word1], 4: ['connInterval', word1], 
                                                   5: ['connLatency', word1], 6: ['connTimeout', word1], 
                                                   7: ['clockAccuracy', byte1]}},

            'GAP Link Terminated': {'command': 0x04, 'opcode': 0x0606, 'plength': 4,
                                    'parameter': {0: ['Status', byte1], 1: ['connHandle', word1], 2: ['reason', byte1]}},

            'Gap Lnk Parameter Update': {'command': 0x04, 'opcode': 0x0607, 'plength': 9,
                                         'parameter': {0: ['Status', byte1], 1: ['connHandle', word1], 
                                                       2: ['connInterval', word1], 3: ['connLatency', word1], 
                                                       4: ['connTimeout', word1]}},

            'GAP Random Address Changed': {'command': 0x04, 'opcode': 0x0608, 'plength': 18,
                                           'parameter': {0: ['Status', byte1], 1: ['addrType', byte1], 2: ['newRandomAddr', byte16]}},

            'GAP Signature Updated': {'command': 0x04, 'opcode': 0x0609, 'plength': 12,
                                      'parameter': {0: ['Status', byte1], 1: ['addrType', byte1], 2: ['devAddr', byte6], 
                                                    3: ['signCounter', word2]}},

            'GAP Authentication Complete': {'command': 0x04, 'opcode': 0x060A, 'plength': 101,
                                            'parameter': {0: ['Status', byte1], 1: ['connHandle', word1], 2: ['authState', byte1], 
                                                          3: ['secInfo', byte1], 4: ['secInfo.LTKsize', byte1], 
                                                          5: ['devSecInfo.LTK', byte16], 6: ['devSecInfo.DIV', word1], 
                                                          7: ['devSecInfo.rand', byte8], 8: ['identityInfo', byte1], 
                                                          9: ['devSecInfo.LTKsize', byte1], 10: ['devSecInfo.LTK', byte16], 
                                                          11: ['devSecInfo.DIV', word1], 12: ['devSecInfo.rand', byte8],
                                                          13: ['identityInfo.IRK', byte16], 14: ['identityInfo.BD_ADDR', byte6], 
                                                          15: ['sigingInfo', byte1], 16: ['signingInfo.IRK', byte16], 
                                                          17: ['signingInfo.signCounter', word1]}},

            'GAP Passkey Needed': {'command': 0x04, 'opcode': 0x060B, 'plength': 11,
                                   'parameter': {0: ['Status', byte1], 1: ['devAddr', byte6], 2: ['connHandle', word1], 
                                                 3: ['uiInputs', byte1], 4: ['uiOutputs', byte1]}},

            'GAP Slave Requested Security': {'command': 0x04, 'opcode': 0x060C, 'plength': 10,
                                             'parameter': {0: ['Status', byte1], 1: ['connHandle', word1], 
                                                           2: ['devAddr', byte6], 3: ['authReq', byte1]}},

            'GAP Device Information': {'command': 0x04, 'opcode': 0x060D, 'plength': 11,
                                       'parameter': {0: ['Status', byte1], 1: ['eventTypes', byte1], 2: ['addrType', byte1], 
                                                     3: ['addr', byte6], 4: ['rssi', byte1], 5: ['dataLen', byte1], 
                                                     6: ['dataField', Nbyte]}},

            'GAP Bond Complete': {'command': 0x04, 'opcode': 0x060E, 'plength': 3,
                                  'parameter': {0: ['Status', byte1], 1: ['connHandle', word1]}},

            'GAP Pairing Requested': {'command': 0x04, 'opcode': 0x060F, 'plength': 8,
                                      'parameter': {0: ['status', byte1], 1: ['connHandle', word1], 2: ['ioCap', byte1], 
                                                    3: ['oobDataFlag', byte1], 4: ['authReq', byte1], 5: ['maxEncKeySize', byte1], 
                                                    6: ['keyDist', byte1]}},

            'CommandStatus': {'command': 0x04, 'opcode': 0x067F, 'plength': 4,
                              'parameter': {0: ['Status', byte1], 1: ['opCode', word1], 2: ['dataLen', byte1], 3: ['payLoad', Nbyte]}},
        }

        self.Opcode_Lookup = {
            0x0600: 'GAP Device Init Done',
            0x0601: 'GAP Device Discovery',
            0x0602: 'GAP Advert Data Update Done',
            0x0603: 'GAP Make Discoverable Done',
            0x0604: 'GAP End Discoverable Done',
            0x0605: 'GAP Link Established',
            0x0606: 'GAP Link Terminated',
            0x0607: 'Gap Lnk Parameter Update',
            0x0608: 'GAP Random Address Changed',
            0x0609: 'GAP Signature Updated',
            0x060A: 'GAP Authentication Complete',
            0x060B: 'GAP Passkey Needed',
            0x060C: 'GAP Slave Requested Security',
            0x060D: 'GAP Device Information',
            0x060E: 'GAP Bond Complete',
            0x060F: 'GAP Pairing Requested',
            0x067F: 'CommandStatus',
        }

        self.ops = CmdEvtOps(self.Commands, self.Opcode_Lookup)

    def Event_Lookup(self, item):
        return self.ops.Event_Lookup(item)

    def Create_Packet(self, cmd, **Parameter):
        return self.ops.Create_Command_Packet(cmd, **Parameter)

    def Decode_Packet(self, commands, packet):
        self.ops.Decode_Packet(commands, packet)


if __name__ == '__main__':
    a = GAP_Vendor_Events()
    a.Create_Packet('GAP Device Discovery', Status=0x00, numDevs=0x00, array=[
                    0x00, 0x01, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06])
    a.Create_Packet('GAP Advert Data Update Done', Status=0x00, adType=0x00)

    a.Decode_Packet(0x060D, [0x00, 0x04, 0x00, [0xBC, 0x6A, 0x29, 0xAB, 0xE7, 0x71], 0xBB, 0x1E,
                             0x1A, 0x09, 0x04c, 0x053, 0x020, 0x053, 0x065, 0x06E, 0x073, 0x06F, 0x072, 0x020, 0x030,
                             0x033, 0x038, 0x036, 0x020, 0x054, 0x03a, 0x02b, 0x032, 0x032, 0x02e, 0x037, 0x034, 0x000, 0x002,
                             0x00a, 0x000])
