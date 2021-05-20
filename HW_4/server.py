from socket import *
import argparse
import pickle
import logging
from log import server_log_config


logger = logging.getLogger('server')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', default='localhost')
    parser.add_argument('port', nargs='?', default=8888)
    return parser


def get_message(data=None):     # Функция переписана под логгирование try except
    if data is not None:
        try:
            data = pickle.loads(data)
            name = data['user']['account_name']
        except Exception as er:
            logger.info(f'Ошибка - {er}')
        else:
            logger.info('Получено сообщение от пользователя %s', name)
        finally:
            return data
    else:
        return "Ничего"


def prepare_response(data=get_message()):
    if data == 'Ничего':
        return "Нет запроса от клиента"
    else:
        if data['action'] == 'presence':
            logger.info('Ответ для пользователя подготовлен')
            return 200


def send_response(data=prepare_response()):
    response = {
                'response': data,
                'alert': 'Вы на сервере'
            }
    logger.info('Вы на сервере')
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
        x = get_message(message)
        prepare_response(x)
        client.send(send_response())
        client.close()
