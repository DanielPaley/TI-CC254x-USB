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



from GAP_Vendor_Events import *
from HCI_EXT_Events import *
import os
import sys
import time
from threading import Thread


class Return_Handler(Thread):

    Device = None
    GVEvents = GAP_Vendor_Events()
    HCIEvents = HCI_EXT_Events()

    def __init__(self, BTDongle=None):
        ''' input the BT USB Dongle connection
        '''
        Thread.__init__(self)
        self.Device = BTDongle
        print "Initialize Return Handler"

        self.PacketOptions = {0x01: self.CommandPacket,
                              0x02: self.AsyncPacket,
                              0x03: self.SyncPacket,
                              0x04: self.EventPacket,
                              }
        self.EventCode = {0xFF: 'HCI_LE_ExtEvent',
                          }

    def CommandPacket(self):
        print "Found Command Packet"

    def AsyncPacket(self):
        print "Found Async Packet"

    def SyncPacket(self):
        print "Found Sync Packet"

    def EventPacket(self):
        print "- Type\t\t : 0x04 (Event)"
        # - should be the start of a new received command/event - lets check
        event_code = ord(self.Device.read(size=1))
        print "- EventCode\t : 0x%x (HCI_LE_ExtEvent)" % (event_code)

        if event_code in self.EventCode:
            # this is the size of incoming packet (remaining)
            Data_Length = ord(self.Device.read(size=1))

            print "- Data Length \t : 0x%.2x (%d) bytes" % (Data_Length, Data_Length)

            event = ord(self.Device.read(size=1))
            event |= ord(self.Device.read(size=1)) << 8

#            print "Event is ",hex(event)
            packet = []

            for i in range(Data_Length - 2):    # we already unstringed event.
                packet.append(ord(self.Device.read(size=1)))

#            print "Packet size is %d"%len(packet)
            if (self.GVEvents.Event_Lookup(event)):
                # we have a GAP Vendor Event - pass to handle
                print "- Event \t : %s (%s)" % (hex(event), self.GVEvents.Event_Lookup(event))
                self.GVEvents.Decode_Packet(event, packet)
            elif self.HCIEvents.Event_Lookup(event):
                # we have a HCI Event - pass to handle
                print "- Event \t : %x : (%s)" % (hex(event), self.HCIEvents.Event_Lookup(event))
                self.HCIEvents.Decode_Packet(event, packet)
            else:
                # Not sure what we have - error condition
                print '*** ERROR *** - received unknown Event ' + str(event_code)
                print " - " + str(packet)
#            print "Packet length remaining %d"%len(packet)

    def run(self):
        while(self.Device.isOpen()):  # Read a new packet
            if (self.Device.inWaiting() > 0):
                print "\n================================================="
                a = ord(self.Device.read(size=1))
                if ((a <= 4) and (a >= 0)):
                    self.PacketOptions[a]()

            time.sleep(1)
