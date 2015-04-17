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




from struct import *

# Nbyte
# 1byte
# 6byte
# 8byte
# 16byte
#
#
# N1byte1byte16byte
# 1word
# 2word
# 3word
# 4word

#-----------------------------------------------------------
# each function - takes in the defined size/type value
# and returns a byte string in the correct
# usable order
#-----------------------------------------------------------


def byte1(data, bytes=False):
    # input is a byte - format of:
    #    0x0e
    #    14

    #    print "Byte1: Data ",type(data),data

    if isinstance(data, list):
        inbyte = data.pop(0)
    else:
        inbyte = data

    if (bytes):
        #        print "Byte1: Data ",inbyte," Type ",type(inbyte)
        a = pack('B', inbyte)
#        print "Sending back ",hex(ord(a))
        return hex(ord(a))

    if isinstance(inbyte, str):
        if ('x' in inbyte):
            a = pack('B', int(data, 16))
        else:   # integer value (decimal?)
            a = pack('B', int(data, 10))
        return a

    elif isinstance(inbyte, list):  # it's an int
        a = inbyte.pop(0)
        a = pack('B', a)
        return a
    else:
        return pack('B', inbyte)


def Nbyte(data, number=None, bytes=False):
    ''' data is a list or ':' seperated values
        need to transform into formated values
       format:
          0x12:0x23:0x34:....
          [0x12,0x23,0x34...]
    '''
    # first resolve data as a list of correct size(number)
#    print "Nbyte - data",data,' number ',number

#    if (bytes):
#        print "NByte: data ",data

    a = []
    if isinstance(data, str):
        if (':' in data):
            # - strip and build bytes
            for i in data.split(":"):
                #                print "Plotting ",i
                a.append(i)
    else:
        a = data

    # ok now size a
#    if (bytes):
#        print "Size is ",number," vs ",len(a)
    if (number == None):
        number = len(a)

    a = a[:number]

    b = []
    for i in a:
        b.append(byte1(i))

#    print "     : data ",data
    return b


def byte6(data, bytes=False):
    #    print "Byte6",data[0]
    a = Nbyte(data, 6)
    return a


def byte8(data, bytes=False):
    #    print "Byte8"
    return Nbyte(data, 8)


def byte16(data, bytes=False):
    #    print "Byte16"
    return Nbyte(data, 16)


def word1(data, bytes=False):
    ''' data is a list of received data bytes
        which we transform into a byte adjusted word
    '''
    b = []

    if isinstance(data, str):
        if ('x' in data):
            a = pack('H', int(data, 16))
        else:   # integer value (decimal?)
            a = pack('H', int(data, 10))

    else:   # type better be int
        if (bytes):
            a = data.pop(0)
            b = data.pop(0)
            a = unpack('H', pack('BB', a, b))
            a = hex(a[0])
        else:
            a = pack('H', data)
            if isinstance(data, list):
                c = data.pop(0)

    return a


def word2(data, bytes=False):
    #    print "word2"
    b = []
    if isinstance(data, str):
        if ('x' in data):
            a = pack('I', int(data, 16))
        else:   # integer value (decimal?)
            a = pack('I', int(data, 10))

    else:   # type better be int
        #        print "Word2 - type ",type(data),data
        a = pack('I', data)

#    for i in a:
#        b.append( hex(ord(i)))

#    return b
    return a


def word3(data, bytes=False):
    #    print "word3"
    b = []
    if isinstance(data, str):
        if ('x' in data):
            a = pack('Q', int(data, 16))
        else:   # integer value (decimal?)
            a = pack('Q', int(data, 10))

    else:   # type better be int
        a = pack('I', data)

    # strip off last two locations
    a = a[:-2]

    for i in a:
        b.append(hex(ord(i)))

    return b


def word4(data, bytes=False):
    #    print "word4"

    b = []
    if isinstance(data, str):
        if ('x' in data):
            a = pack('Q', int(data, 16))
        else:   # integer value (decimal?)
            a = pack('Q', int(data, 10))

    else:   # type better be int
        a = pack('I', data)

    for i in a:
        b.append(hex(ord(i)))

    return b


def N1byte1byte6byte(data, bytes=False):
    # special return 'event' routine.....
    # datainput is a list
    #    print "N1byte1byte6byte"

    #    if (bytes):
    #        print "Data ",data
    ary = []
    while data:
        ary.append(byte1(data.pop(0)))
        ary.append(byte1(data.pop(0)))
        ary += byte6(data[:6])
        del data[:6]

    return ary


#a = [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,0x10]
#
# print "1 ",byte1(a)
#a = [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,0x10]
# print "6 ",byte6(a)
#a = [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,0x10]
# print "16 ",byte16(a)
#a = [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,0x10]
# print 'word\n'
#a = [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,0x10]
# print '1 ',hex(word1(a))
#a = [0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08,0x09,0x0A,0x0B,0x0C,0x0D,0x0E,0x0F,0x10]
# print '2 ',hex(word2(a))
#
#a = [0x99,0x98,0x01,0x02,0x03,0x04,0x05,0x06]
# print '3 ',N1byte1byte6byte(a)
