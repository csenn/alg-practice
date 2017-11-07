import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket'
    sys.exit()

print 'Socket Created'

host = 'www.google.rs'
port = 80

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print 'eheh'
    sys.exit()

print 'Ip address of {0} is {1}'.format(host, remote_ip)

s.connect((remote_ip, port))

print 'Socket connected'

message = "GET / HTTP/1.1\r\n\r\n"

try:
    s.sendall(message)
except socket.error:
    print 'Send Falied'
    sys.exit()

print 'Message Sent'

#Now receive data
reply = s.recv(4096)

print reply

s.close()