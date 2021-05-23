import logging


logger = logging.getLogger('client')
formatter = logging.Formatter("%(asctime)s - %(levelname)s -  %(module)s - %(message)s")
fh = logging.FileHandler('client.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    logger.info('Тестовый запуск логирования')