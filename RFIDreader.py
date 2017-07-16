#!/usr/bin/python
import time,serial
from termcolor import cprint

banner = "+++++++++++++++++++++++++++++++++++\n"
banner+= "+	    RFID Reader           +\n"
banner+= "+         @mohammadaskar2         +\n"
banner+= "+++++++++++++++++++++++++++++++++++\n"

cprint(banner,"red")
cprint("[+]started at {0}\n".format(time.ctime()),"blue")

# change the USB serial to the reader serial.

serial = serial.Serial("/dev/ttyUSB0", baudrate=9600) 
code = ''
readnum = 1
while True:
        data = serial.read()
        if data == '\r':
                cprint("[+]Read number {0} for the card is {1}".format(readnum,str(code.strip("\n"))),"green")
		readnum = readnum + 1
		code = ''
        else:
                code = code + data
