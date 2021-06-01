import logging
from logging import handlers

logger = logging.getLogger('server')
formatter = logging.Formatter("%(asctime)s - %(levelname)s -  %(module)s - %(message)s")

fht = logging.FileHandler("server.log")
fht.setLevel(logging.DEBUG)
fht.setFormatter(formatter)

tr = logging.handlers.TimedRotatingFileHandler('server.log', interval=1, when='D')
tr.setLevel(logging.DEBUG)
tr.setFormatter(formatter)

# logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
logger.addHandler(tr)


if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')