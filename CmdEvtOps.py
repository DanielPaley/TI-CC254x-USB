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
from struct import *


class CmdEvtOps():

    def __init__(self, cmd, opcode):
        self.Command = cmd
        self.Opcode_Lookup = opcode


    def Create_Command_Packet(self, Cmd, **Parameter):
        '''first lookup opcode for # parameters and order
        then construct packet.  Return string
        '''
        frame = []

        packetFrame = {}
        print Cmd
        packetFrame = self.Command[Cmd]
        pktparms = packetFrame['parameter']

        frame += byte1(packetFrame['command'])  # command packet type
        frame += word1(packetFrame['opcode'])
        frame += byte1(packetFrame['plength'])

        for index in sorted(pktparms.keys()):
            if (Parameter.get(pktparms[index][0]) == None):
                print "***ERROR*** Missing parameter %s" % pktparms[index]
                exit(1)
            # print "index [",index,"] pktparms[]",pktparms[index][0],'parameer
            # ',Parameter.get(pktparms[index][0])
            value = Parameter.get(pktparms[index][0])
            frame += pktparms[index][1](value)

#            frame.append(Parameter.get(pktparms[index][0]))

        outgoing = ''
        for item in frame:
            outgoing += item

#        print "Frame is ",frame,'\n'
        i = 1
        pt = ''
        for thing in frame:

            pt += "0x%.2x " % ord(thing)
#            pt += ' ',thing
            i += 1
            if ((i % 10) == 0):
                print "\t", pt
                pt = ''
                i = 1

        if (len(pt) > 0):
            print "\t", pt
        print

        return outgoing

    def Event_Lookup(self, item):
        ''' if item in Events, return true
        '''
        if (item in self.Opcode_Lookup):
                # print "Event Lookup ",hex(item),' ',self.Opcode_Lookup[item]
            return self.Opcode_Lookup[item]
        else:
            return None

    def Decode_Packet(self, event, packet):
        ''' decode the incoming packet based upon the event code
        '''

        # 'GAP Device Information' : {'command':0x04, 'opcode':0x060D,
        #'parameter' : {0:'Status',1:'eventTypes',2:'addrType',3:'addr',4:'rssi',5:'dataLen',6:'dataField'}},

        a = self.Opcode_Lookup[event]

        pkt_format = self.Command[a]

        # events : type(event),eventcode,data length, event, status, opcode,
        # datalength, dump

#            print "- Type   \t\t : 0x0004 : (Event)"
#            print "- Opcode \t\t : 0x%.4x   %s"%(event,a)

        for i in sorted(pkt_format['parameter']):
            if (len(packet) > 0):
                #                    print "Type to decode",pkt_format['parameter'][i],"Packet rec ",packet
                #                    print "..",pkt_format['parameter'][i]
                a = (pkt_format['parameter'][i][1](data=packet, bytes=True))
                if isinstance(a, list):
                    #                        print "Found List"
                    b = ''
                    formatcount = 1
                    c = ''
                    listLSS = False
                    for ijk in a:
                        b += hex(ord(ijk))[2:] + ':'
                        if ((formatcount % 16) == 0):
                            b += '\n\t\t : '
                            formatcount = 1
                        else:
                            formatcount += 1

                        if ((ord(ijk) >= 0x20) and (ord(ijk) <= 0x7E)):
                           # if (ord(ijk) == 0x4c):
                            listLSS = True
                            if (listLSS):
                                c += chr(ord(ijk))
# print "  %s \t : %s  \t\t:%d" %
# (pkt_format['parameter'][i][0].ljust(10,' '), b,len(packet))
                    b = b[:-1]
                    print "  %s \t : %s" % (pkt_format['parameter'][i][0].ljust(10, ' '), b)
                    if (listLSS):
                        print " + %s " % (c)
                else:
                    #                        print "Type ",type(a),len(a)
                    # print "  %s \t : %s \t\t:%d" %
                    # (pkt_format['parameter'][i][0].ljust(10,' '),
                    # (a),len(packet))
                    print "  %s \t : %s" % (pkt_format['parameter'][i][0].ljust(10, ' '), (a))
            else:
                break


if __name__ == '__main__':
    print 'Main'
    Opcode_Lookup = {0xFE00: 'GAP Device Initialization'}
    Command = {
        'GAP Device Initialization': {'command': 0x01, 'opcode': 0xFE00, 'plength': 36,
                                      'parameter': {0: ['profileRole', byte1], 1: ['maxScanResponses', byte1], 2: ['IRK', byte16],
                                                    3: ['CSRK', byte16], 4: ['signCounter', word2]}},

        'GAP Configure Device Address': {'command': 0x01, 'opcode': 0x0FE03, 'plength': 7,
                                         'parameter': {0: ['addrType', byte1], 1: ['Addr', byte6]}},

        'GAP Device Discovery Request': {'command': 0x01, 'opcode': 0x0FE04, 'plength': 3,
                                         'parameter': {0: ['mode', byte1], 1: ['activeScan', byte1], 2: ['whiteList', byte1]}}}

    a = CmdEvtOps(Command, Opcode_Lookup)
    a.Create_Command_Packet(
        'GAP Device Discovery Request', mode=0, activeScan=0, whileList=0)
