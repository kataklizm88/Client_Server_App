from socket import *
import json
import time
import argparse
import pickle


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', default='localhost')
    parser.add_argument('port', nargs='?', default=8888)
    return parser


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


def send_presence(data = make_presence()):
    data = pickle.dumps(data)
    return data

def get_response(data = None):
    data = pickle.loads(data)
    res = data['alert']
    return res

if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((namespace.addr, namespace.port))
    s.send(send_presence())
    response = s.recv(100000)
    print(get_response(response))
    s.close()
