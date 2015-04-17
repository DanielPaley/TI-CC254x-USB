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


class GATT_Vendor_Commands():

    def __init__(self):
        print "Init Command Format"

        self.Commands = {
            'GATT_ExchangeMTU': {'command': 0x01, 'opcode': 0xFD82, 'plength': 4,
                                 'parameter': {0: ['connHandle', word1], 1: ['clientRxMTU', word1]}},

            'GAT_DiscAllPrimaryServices': {'command': 0x01, 'opcode': 0xFD90, 'plength': 2,
                                           'parameter': {0: ['connHandle', word1]}},

            'GATT_Disc_Primary_Service_By_UUID': {'command': 0x01, 'opcode': 0xFD86, 'plength': 2,
                                                  'parameter': {0: ['connHandle', word1], 1: ['value', Nbyte]}},

            'GATT_FindIncluded_Services': {'command': 0x01, 'opcode': 0xFDB0, 'plength': 6,
                                           'parameter': {0: ['connHandle', word1], 1: ['startHandle', word1], 
                                                         2: ['endHandle', word1]}},

            'GATT_Disc_All_Chars': {'command': 0x01, 'opcode': 0xFDB2, 'plength': 6,
                                    'parameter': {0: ['connHandle', word1], 1: ['startHandle', word1], 
                                                  2: ['endHandle', word1]}},

            'GATT_DiscCharsByUUID': {'command': 0x01, 'opcode': 0xFD88, 'plength': 6,
                                     'parameter': {0: ['connHandle', word1], 1: ['startHandle', word1], 
                                                   2: ['endHandle', word1], 3: ['type', Nbyte]}},

            'GATT_DiscAllCharDescs': {'command': 0x01, 'opcode': 0xFD84, 'plength': 6,
                                      'parameter': {0: ['connHandle', word1], 1: ['startHandle', word1], 
                                                    2: ['endHandle', word1]}},

            'GATT_ReadCharValue': {'command': 0x01, 'opcode': 0xFD8A, 'plength': 4,
                                   'parameter': {0: ['connHandle', word1], 1: ['handle', word1]}},

            'GATT_ReadUsingCharUUID': {'command': 0x01, 'opcode': 0xFDB4, 'plength': 6,
                                       'parameter': {0: ['connHandle', word1], 1: ['startHandle', word1], 
                                                     2: ['endHandle', word1], 3: ['type', Nbyte]}},

            'GATT_ReadLongCharValue': {'command': 0x01, 'opcode': 0xFD8C, 'plength': 6,
                                       'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 
                                                     2: ['offset', word1]}},

            'GATT_ReadMultiCharValues': {'command': 0x01, 'opcode': 0xFD8E, 'plength': 4,
                                         'parameter': {0: ['connHandle', word1], 1: ['handles', word1]}},

            'GATT_WriteNoRsp': {'command': 0x01, 'opcode': 0xFDB6, 'plength': 4,
                                'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 2: ['value', Nbyte]}},

            'GATT_SignedWriteNoRsp': {'command': 0x01, 'opcode': 0xFDB8, 'plength': 4,
                                      'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 2: ['value', Nbyte]}},

            'GATT_WriteCharValue': {'command': 0x01, 'opcode': 0xFD92, 'plength': 2,
                                    'parameter': {0: ['connHandle', word1]}},

            'GATT_WriteLongCharValue': {'command': 0x01, 'opcode': 0xFD96, 'plength': 6,
                                        'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 
                                                      2: ['offset', word1], 3: ['value', Nbyte]}},

            'GATT_ReliableWrites': {'command': 0x01, 'opcode': 0xFDBA, 'plength': 3,
                                    'parameter': {0: ['connHandle', word1], 1: ['numRequests', byte1], 
                                                  2: ['requests', Nbyte]}},

            'GATT_ReadCharDesc': {'command': 0x01, 'opcode': 0xFDBC, 'plength': 4,
                                  'parameter': {0: ['connHandle', word1], 1: ['handle', word1]}},

            'GATT_ReadLongCharDesc': {'command': 0x01, 'opcode': 0xFDBE, 'plength': 6,
                                      'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 
                                                    2: ['offset', word1]}},

            'GATT_WriteCharDesc': {'command': 0x01, 'opcode': 0xFDC0, 'plength': 6,
                                   'parameter': {0: ['connHandle', word1], 1: ['signature', byte1], 
                                                 2: ['command', byte1], 3: ['handle', word1], 4: ['value', Nbyte]}},

            'GATT_WriteLongCharDesc': {'command': 0x01, 'opcode': 0xFDC2, 'plength': 6,
                                       'parameter': {0: ['connHandle', word1], 1: ['handle', word1], 
                                                     2: ['offset', word1], 3: ['value', Nbyte]}},

            'GATT_Notification': {'command': 0x01, 'opcode': 0xFD9B, 'plength': 5,
                                  'parameter': {0: ['connHandle', word1], 1: ['authenticated', byte1], 
                                                2: ['handle', word1], 3: ['value', Nbyte]}},

            'GATT_Indication': {'command': 0x01, 'opcode': 0xFD9D, 'plength': 5,
                                'parameter': {0: ['connHandle', word1], 1: ['authenticated', byte1], 
                                              2: ['handle', word1], 3: ['value', Nbyte]}},

            'GATT_AddService': {'command': 0x01, 'opcode': 0xFDFC, 'plength': 6,
                                'parameter': {0: ['connHandle', word1], 1: ['uuid', word1], 1: ['numAttrs', word1]}},

            'GATT_DelService': {'command': 0x01, 'opcode': 0xFDFD, 'plength': 4,
                                'parameter': {0: ['connHandle', word1], 1: ['handle', word1]}},

            'GATT_AddAttribute': {'command': 0x01, 'opcode': 0xFDFE, 'plength': 3,
                                  'parameter': {0: ['connHandle', word1], 1: ['uuid', Nbyte], 2: ['permissions', byte1]}},

        }

        self.Opcode_Lookup = {
            0xFD82: 'GATT_ExchangeMTU',
            0xFD90: 'GAT_DiscAllPrimaryServices',
            0xFD86: 'GATT_Disc_Primary_Service_By_UUID',
            0xFDB0: 'GATT_FindIncluded_Services',
            0xFDB2: 'GATT_Disc_All_Chars',
            0xFD88: 'GATT_DiscCharsByUUID',
            0xFD84: 'GATT_DiscAllCharDescs',
            0xFD8A: 'GATT_ReadCharValue',
            0xFDB4: 'GATT_ReadUsingCharUUID',
            0xFD8C: 'GATT_ReadLongCharValue',
            0xFD8E: 'GATT_ReadMultiCharValues',
            0xFDB6: 'GATT_WriteNoRsp',
            0xFDB8: 'GATT_SignedWriteNoRsp',
            0xFD92: 'GATT_WriteCharValue',
            0xFD96: 'GATT_WriteLongCharValue',
            0xFDBA: 'GATT_ReliableWrites',
            0xFDBC: 'GATT_ReadCharDesc',
            0xFDBE: 'GATT_ReadLongCharDesc',
            0xFDC0: 'GATT_WriteCharDesc',
            0xFDC2: 'GATT_WriteLongCharDesc',
            0xFD9B: 'GATT_Notification',
            0xFD9D: 'GATT_Indication',
            0xFDFC: 'GATT_AddService',
            0xFDFD: 'GATT_DelService',
            0xFDFE: 'GATT_AddAttribute',

        }

        self.ops = CmdEvtOps(self.Commands, self.Opcode_Lookup)

    def Event_Lookup(self, item):
        return self.ops.Event_Lookup(item)

    def Create_Packet(self, cmd, **Parameter):
        return self.ops.Create_Command_Packet(cmd, **Parameter)

    def Decode_Packet(self, event, packet):
        self.ops.Decode_Packet(event, packet)


if __name__ == '__main__':
    a = GATT_Vendor_Commands()
    a.Create_Packet(
        'GATT_ReadLongCharDesc', connHandle=0x00, handle=0x01, offset=0x02)
