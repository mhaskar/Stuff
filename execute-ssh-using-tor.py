#!/usr/bin/python

```
execute SSH command using tor script
author : Mohammad Askar
@mohammadaskar2
```

import socket,socks,paramiko 

def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150) 
socket.socket = socks.socksocket 
socket.create_connection = create_connection 

username = "username"
passwd = "password"
host = "ssh.server.com"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())
ssh.connect(host , 22, username=username, 
    password=passwd)
while True:
    command = raw_input("%s@SafeBox:>>"%username)   
    stdin, stdout, stderr = ssh.exec_command(command)
    print stdout.read().strip("\n")
