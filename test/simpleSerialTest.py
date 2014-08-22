#! /usr/bin/python

import serial
srl = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
i = 0
while i<20:
#    srlin = srl.read(20)
#    print(srlin)
    print(srl.readline())
    i = i + 1
srl.close()