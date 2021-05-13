from socket import *
import json
import time
from sys import argv


if len(argv) > 1:
    name, addr, port = argv
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((str(addr), int(port)))
else:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8888))

def make_presence(action='presence', name='User'):
    presence = {
        "action": action,
        "time": time.ctime(time.time()),
        "type": "status",
        "user": {
                "account_name":  name,
                "status":      "Yep, I am here!"
                }
        }
    return presence

def send_presence():
    return s.send(json.dumps(make_presence()).encode('utf-8'))


def get_response(data=None):
    response = s.recv(1000000)
    if response:
        data = response
        data = json.loads(data)
        res = data['alert']
        return res


send_presence()
print(get_response())
s.close()