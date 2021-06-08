from functools import wraps
import logging
from log_decor import log_decor_config
import inspect

logger = logging.getLogger('decorator')


def log(func):
  @wraps(func)
  def deco(*args, ** kvargs):
    current_frame = inspect.currentframe()
    caller_frame = current_frame.f_back
    code_obj = caller_frame.f_code
    code_obj_name = code_obj.co_name
    """ Для задачи №1 """
    logger.info('Имя функции: %s, ее аргументы: %s', func.__name__, args)
    """ Для задачи №2 """
    logger.info('Функция %s вызвана из функции %s', func.__name__, code_obj_name)
    return func(*args, **kvargs)
  return deco

@log
def func(x=None):
  return f'Just a function with attribute {x}'

def main():
  print(func())

if __name__ == "__main__":
  main()