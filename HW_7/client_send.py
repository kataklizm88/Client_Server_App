from socket import *
import argparse
import logging
from log import client_log_config


logger = logging.getLogger('client')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', default='localhost')
    parser.add_argument('port', nargs='?', default=8888)
    return parser

def get_socket():
    parser = create_parser()
    namespace = parser.parse_args()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((namespace.addr, namespace.port))
    return sock


def send_msg(s):
    msg = input("Введите ваше сообщение или напишите exit для выхода ")
    logger.info('Сообщение отправлено в чат')
    return s.send(msg.encode('utf-8'))


def get_msg(s):
    data = s.recv(1024).decode('utf-8')
    if data == 'exit':
        return data
    else:
        logger.info('Получено сообщение из чата')
        print('Сообщение из чата: ', data)


def main():
    s = get_socket()
    while True:
        send_msg(s)
        x = get_msg(s)
        if x == 'exit':
            print('сеанс завершен')
            break


if __name__ == "__main__":
    """ Клиент для отправки сообщений """
    main()