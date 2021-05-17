from socket import *
import json
from sys import argv


if len(argv) > 1:
    name, addr, port = argv
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((str(addr), int(port)))
    s.listen(5)
else:
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('localhost', 8888))
    s.listen(5)

while True:
    client, addr = s.accept()

    def get_message(data=None):
        message = client.recv(1000000)
        if message:
            data = message
            data = json.loads(data)
            return data

    def prepare_response(data=None):
        data = get_message()
        answer = None
        if data['action'] == 'presence':
            answer = 200
        return answer

    def send_response(data=None):
        data = prepare_response()
        response = {
                    'response': data,
                    'alert': 'Вы на сервере'
                }
        return client.send(json.dumps(response).encode('utf-8'))

    send_response()
    client.close()

