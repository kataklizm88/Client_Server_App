from socket import *
import argparse
import select
import logging
from log import server_log_config

logger = logging.getLogger('server')


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', default='localhost')
    parser.add_argument('port', nargs='?', default=8888)
    return parser


def read_requests(r_clients, all_clients):
   responses = {}

   for sock in r_clients:
       try:
           data = sock.recv(1024).decode('utf-8')
           responses[sock] = data
           logger.info('Получен запрос')
       except:
           print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
           all_clients.remove(sock)

   return responses

def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            try:
                resp = requests[sock].encode('utf-8')
                for i in all_clients:
                    i.send(resp)
            except:
                print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
                sock.close()
                all_clients.remove(sock)


def main():
    clients = []
    parser = create_parser()
    namespace = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((namespace.addr, namespace.port))
    s.listen(5)
    s.settimeout(0.2)
    while True:
      try:
        client, addr = s.accept()
      except OSError as e:
          pass
      else:
          logger.info("Получен запрос на соединение от %s" % str(addr))
          print("Получен запрос на соединение от %s" % str(addr))
          clients.append(client)
      finally:
          wait = 10
          r = []
          w = []
          try:
              r, w, e = select.select(clients, clients, [], wait)
          except:
              pass
          requests = read_requests(r, clients)
          if requests:
              write_responses(requests, w, clients)


if __name__ == "__main__":
    main()


