from socket import *
import json
from sys import argv


name, ip, port = argv
s = socket(AF_INET, SOCK_STREAM)
s.bind((str(ip), int(port)))
s.listen(5)

while True:
    client, addr = s.accept()

    def get_message():
        data = client.recv(1000000)
        data = json.loads(data)
        return data

    def prepare_response():
        data = get_message()
        answer = None
        if data['action'] == 'presence':
            answer = 200
        return answer

    def send_response():
        data = prepare_response()
        response = {
                    'response': data,
                    'alert': 'Вы на сервере'
                }
        return client.send(json.dumps(response).encode('utf-8'))


    send_response()
    client.close()




