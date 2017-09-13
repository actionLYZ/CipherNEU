# Python use C function dll
# UKey by C
# -*- coding: UTF-8 -*-

import os
from ctypes import *
import ctypes

C = ctypes.CDLL("Ukey.dll")
# C.Hello()

Disk_Num = C.GetNum()

key = "This is the key"

size = len(key)

def Write(key):

    C.WriteDisk(key.encode('ASCII'),0x200,size,Disk_Num)
    # return len(key)

def Read(size):
    C.ReadDisk_P.restype = ctypes.c_char_p
    readbuf = C.ReadDisk_P(0x200,size,Disk_Num)
    result = str(readbuf)
    return result

"""
readbuf = C.ReadDisk_P(0x200,size,Disk_Num)

readbuf = ctypes.string_at(readbuf, -1)

result = readbuf.decode('utf-8')
"""
# result = result.value
# result = str(readbuf)

str = Read(size)
str = str[2:2 + size]

print (str)

"""
for i in range(len(result)):
    print (result[i])
"""
# print (result)
# print (readbuf)



