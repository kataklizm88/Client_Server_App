from socket import *
import json
import argparse
import pickle


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', default='localhost')
    parser.add_argument('port', nargs='?', default=8888)
    return parser


def get_message(data=None):
    if data is not None:
        data = pickle.loads(data)
        return data
    else:
        return "Ничего"


def prepare_response(data=get_message()):  # Версия для теста
    if data == 'Ничего':
        return "Нет запроса от клиента"
    else:
        if data['action'] == 'presence':
            return 200


def send_response(data=prepare_response()):
    response = {
                'response': data,
                'alert': 'Вы на сервере'
            }
    return pickle.dumps(response)


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((namespace.addr, namespace.port))
    s.listen(5)
    while True:
        client, addr = s.accept()
        message = client.recv(1000000)
        get_message(message)
        client.send(send_response())
        client.close()

