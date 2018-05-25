#!/usr/bin/python3
import socket
s = socket.socket()
s.settimeout(5)

target = 'ad.samsclass.info'

username = 'root'  #'foo'
password = 'password'  #'toor'  #'bar'

# Copy from request headers of POST
req = """POST /python/login1.php HTTP/1.1
Host: ad.samsclass.info
Connection: keep-alive
Content-Length: {}
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: null
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Language: en-US,en;q=0.9
Cookie: __cfduid=d9813102a20df9a456a0173649766ee001526962474

u={}&p={}""".format(str(len(username) + len(password) + 5), username, password)
s.connect((target, 80))
#s.send(str.encode(f'HEAD / HTTP/1.1\nHost: {target}\n\n'))
s.send(req.encode())
print(s.recv(1024).decode())
s.close()
