import time
from socket import *
import argparse
import pickle
import logging
from log import client_log_config
from threading import Thread
from queue import Queue

""" Первый вариант: попытка сделать с очередью
    Прилетает только одно сообщение, если сообщений было несколько - второе выйдет только после следующего input.
"""
logger = logging.getLogger('client')

class WorkerThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_queue = Queue()

    def send(self, item):
        self.input_queue.put(item)

    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()

    def run(self):
        while True:
            item = self.input_queue.get()
            if item is None:
                break
            print(item)
            self.input_queue.task_done()
        self.input_queue.task_done()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', default='localhost')
    parser.add_argument('port', nargs='?', default=8888)
    return parser

def true_choise(true_answer, presence):
      while True:
        start = input('Ваш выбор ')
        if start in true_answer:
            if start == 'M':
                message = input('Введите ваше сообщение: ')
                presence['action'] = 'send_all'
                presence['message'] = message
            elif start == 'G':
                group_choise = input('Введите 4-значный номер группы ')
                message = input('Ваше сообщение группе ')
                presence['action'], presence['group'] = 'send_group', group_choise
                presence['message'] = message
            elif start == 'EG':
                group_number = input('Введите номер группы ')
                presence['action'], presence['group'] = 'enter a group', group_number
            break
        else:
            print('Вы ввели некорректные данные попробуйте еще раз')
      logger.info('Сообщение готово')
      return presence

def send_data(s, data):
    logger.info('Сообщение отправлено')
    return s.send(pickle.dumps(data))


def get_data(s):
    logger.info('Получено сообщение от сервера')
    return (pickle.loads(s.recv(1024)))


def main():
    true_answer = ['M', 'G', 'EG']
    presence = {
        "action": 'action',
        "time": time.ctime(time.time()),
        "type": "status",
        "user": 'vlad',
        'group': None,
        'message': None
    }

    parser = create_parser()
    namespace = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((namespace.addr, namespace.port))
    w = WorkerThread()
    w.start()
    while True:
        print("Выберите что хотите сделать:"
            " M - отправить сообщение всем пользователям;"
            " G - отправить сообщение группе; EG - вступить в группу")
        choise = true_choise(true_answer, presence)
        send_data(s, choise)
        w.send(get_data(s))



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error('Ошибка: ', e)