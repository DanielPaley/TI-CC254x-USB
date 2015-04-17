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


class ATT_Vendor_Commands():

    def __init__(self):
        print "Init Command Format"
        self.Commands = {
            'ATT_ErrorRsp': {'command': 0x01, 'opcode': 0xFD01, 'plength': 6,
                             'parameter': {0: ['connHandle', word1], 1: ['reqOpcode', byte1], 2: ['handle', word1], 
                                           3: ['errorCode', byte1]}},

            'ATT_ExchangeMTUReq': {'command': 0x01, 'opcode': 0xFD02, 'plength': 4,
                                   'parameter': {0: ['connHandle', word1], 1: ['clientRxMtu', word1]}},

            'ATT_ExchangeMTURsp': {'command': 0x01, 'opcode': 0xFD03, 'plength': 4,
                                   'parameter': {0: ['connHandle', word1], 1: ['serverRxMTU', word1]}},

            'ATT_FindInfoReq': {'command': 0x01, 'opcode': 0xFD04, 'plength': 6,
                                'parameter': {0: ['connHandle', word1], 1: ['startHandle', word1], 2: ['endHandle', word1]}},

            'ATT_FindINfoRsp': {'command': 0x01, 'opcode': 0xFD05, 'plength': 3,
                                'parameter': {0: ['connHandle', word1], 1: ['format', byte1], 2: ['info', Nbyte]}},

            'ATT_FindByTypeValueReq': {'command': 0x01, 'opcode': 0xFD06, 'plength': 8,
                                       'parameter': {0: ['connHandle', word1], 1: ['startHandle', word1], 2: ['endHandle', word1], 
                                                     3: ['type', word1], 4: ['value', Nbyte]}},

            'ATT_FindByTypeValueRsp': {'command': 0x01, 'opcode': 0xFD07, 'plength': 2,
                                       'parameter': {0: ['connHandle', word1], 1: ['handlesInfo', Nbyte]}},

            'ATT_ReadByTypeReq': {'command': 0x01, 'opcode': 0xFD08, 'plength': 6,
                                  'parameter': {0: ['connHandle', word1], 1: ['startHandle', word1], 2: ['endHandle', word1], 
                                                3: ['type', Nbyte]}},

            'ATT_ReadByTypeRsp': {'command': 0x01, 'opcode': 0xFD09, 'plength': 3,
                                  'parameter': {0: ['connHandle', word1], 1: ['length', byte1], 2: ['dataList', Nbyte]}},

            'ATT_ReadReq': {'command': 0x01, 'opcode': 0xFD0A, 'plength': 4,
                            'parameter': {0: ['connHandle', word1], 1: ['handle', word1]}},

            'ATT_ReadRsp': {'command': 0x01, 'opcode': 0xFD0B, 'plength': 2,
                            'parameter': {0: ['connHandle', word1], 2: ['value', Nbyte]}},

            'ATT_ReadBlobReq': {'command': 0x01, 'opcode': 0xFD0C, 'plength': 6,
                                'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 2: ['offset', word1]}},

            'ATT_ReadBlobRsp': {'command': 0x01, 'opcode': 0xFD0D, 'plength': 2,
                                'parameter': {0: ['connHandle', word1], 1: ['value', Nbyte]}},

            'ATT_ReadMultiReq': {'command': 0x01, 'opcode': 0xFD0E, 'plength': 2,
                                 'parameter': {0: ['connHandle', word1], 1: ['handles', Nbyte]}},

            'ATT_ReadMultiRsp': {'command': 0x01, 'opcode': 0xFD0F, 'plength': 2,
                                 'parameter': {0: ['connHandle', word1], 1: ['values', Nbyte]}},

            'ATT_ReadByGrpTypeReq': {'command': 0x01, 'opcode': 0xFD10, 'plength': 6,
                                     'parameter': {0: ['connHandle', word1], 2: ['startHandle', word1], 3: ['endHandle', word1],
                                                   4: ['groupType', Nbyte]}},

            'ATT_ReadByGrpTypeRsp': {'command': 0x01, 'opcode': 0xFD11, 'plength': 3,
                                     'parameter': {0: ['connHandle', word1], 1: ['length', byte1], 2: ['dataList', Nbyte]}},

            'ATT_WriteReq': {'command': 0x01, 'opcode': 0xFD12, 'plength': 6,
                             'parameter': {0: ['connHandle', word1], 1: ['signature', byte1], 2: ['command', byte1], 
                                           3: ['handle', word1], 4: ['value', Nbyte]}},

            'ATT_WriteRsp': {'command': 0x01, 'opcode': 0xFD13, 'plength': 2,
                             'parameter': {0: ['connHandle', word1]}},

            'ATT_PrepareWriteReq': {'command': 0x01, 'opcode': 0xFD16, 'plength': 6,
                                    'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 2: ['offset', word1], 
                                                  3: ['value', Nbyte]}},

            'ATT_PrepareWriteRsp': {'command': 0x01, 'opcode': 0xFD17, 'plength': 6,
                                    'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 2: ['offset', word1], 
                                                  3: ['value', Nbyte]}},

            'ATT_ExecuteWriteReq': {'command': 0x01, 'opcode': 0xFD18, 'plength': 3,
                                    'parameter': {0: ['connHandle', word1], 1: ['flags', byte1]}},

            'ATT_ExecuteWriteRsp': {'command': 0x01, 'opcode': 0xFD19, 'plength': 2,
                                    'parameter': {0: ['connHandle', word1]}},

            'ATT_HandleValueNotification': {'command': 0x01, 'opcode': 0xFD1B, 'plength': 5,
                                            'parameter': {0: ['connHandle', word1], 1: ['authenticated', byte1], 2: ['handle', word1],
                                                          3: ['value', Nbyte]}},

            'ATT_HandleValueIndicatin': {'command': 0x01, 'opcode': 0xFD1D, 'plength': 5,
                                         'parameter': {0: ['connHandle', word1], 1: ['authenticated', byte1], 2: ['handle', word1], 
                                                       3: ['value', Nbyte]}},

            'ATT_HandleValueConfirmatin': {'command': 0x01, 'opcode': 0xFD1E, 'plength': 2,
                                           'parameter': {0: ['connHandle', word1]}}
        }

        self.Opcode_Lookup = {
            0xFD01: 'ATT_ErrorRsp',
            0xFD02: 'ATT_ExchangeMTUReq',
            0xFD03: 'ATT_ExchangeMTURsp',
            0xFD04: 'ATT_FindInfoReq',
            0xFD05: 'ATT_FindINfoRsp',
            0xFD06: 'ATT_FindByTypeValueReq',
            0xFD07: 'ATT_FindByTypeValueRsp',
            0xFD08: 'ATT_ReadByTypeReq',
            0xFD09: 'ATT_ReadByTypeRsp',
            0xFD0A: 'ATT_ReadReq',
            0xFD0B: 'ATT_ReadRsp',
            0xFD0C: 'ATT_ReadBlobReq',
            0xFD0D: 'ATT_ReadBlobRsp',
            0xFD0E: 'ATT_ReadMultiReq',
            0xFD0F: 'ATT_ReadMultiRsp',
            0xFD10: 'ATT_ReadByGrpTypeReq',
            0xFD11: 'ATT_ReadByGrpTypeRsp',
            0xFD12: 'ATT_WriteReq',
            0xFD13: 'ATT_WriteRsp',
            0xFD16: 'ATT_PrepareWriteReq',
            0xFD17: 'ATT_PrepareWriteRsp',
            0xFD18: 'ATT_ExecuteWriteReq',
            0xFD19: 'ATT_ExecuteWriteRsp',
            0xFD1B: 'ATT_HandleValueNotification',
            0xFD1D: 'ATT_HandleValueIndicatin',
            0xFD1E: 'ATT_HandleValueConfirmatin'
        }

        self.ops = CmdEvtOps(self.Commands, self.Opcode_Lookup)

    def Event_Lookup(self, item):
        return self.ops.Event_Lookup(item)

    def Create_Packet(self, cmd, **Parameter):
        return self.ops.Create_Command_Packet(cmd, **Parameter)

    def Decode_Packet(self, event, packet):
        self.ops.Decode_Packet(event, packet)


if __name__ == '__main__':
    a = ATT_Vendor_Commands()
    a.Create_Packet('ATT_ReadReq', connHandle=0x00, handle=0x01)
