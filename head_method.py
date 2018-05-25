#!/usr/bin/python3
import socket
s = socket.socket()
s.settimeout(2)

target = 'ad.samsclass.info'

s.connect((target, 80))
s.send(str.encode(f'HEAD / HTTP/1.1\nHost: {target}\n\n'))
print(s.recv(1024).decode('utf8'))
s.close()
