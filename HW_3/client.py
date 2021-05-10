from socket import *
import json
import time
from sys import argv


name, addr, port = argv
s = socket(AF_INET, SOCK_STREAM)
s.connect((str(addr), int(port)))

def make_presence():
    presence = {
        "action": 'presence',
        "time": time.time(),
        "type": "status",
        "user": {
                "account_name":  "C0deMaver1ck",
                "status":      "Yep, I am here!"
                }
        }

    return presence


def send_presence():
    return s.send(json.dumps(make_presence()).encode('utf-8'))


def get_response():
    response = s.recv(1000000)
    response = json.loads(response)
    res = response['alert']
    return res


send_presence()
print(get_response())


s.close()

