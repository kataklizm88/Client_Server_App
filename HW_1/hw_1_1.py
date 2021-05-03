import subprocess
import locale

''' Задание № 1'''

list = ['разработка', 'сокет', 'декоратор']
list_Uni = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
            '\u0441\u043e\u043a\u0435\u0442',
            '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
for i in range(len(list)):
    if list[i] == list_Uni[i]:
        print(f'Слово {list[i]} - ', type(list[i]),
              f'Слово {list[i]} - ', type(list[i]), '; Данные совпали')


''' Задание № 2'''
bytes_world = [b'class', b'function', b'method']
for i in bytes_world:
    print(i, type(i), len(i))

''' Задание № 3'''
list = [b'attribute', b'класс', b'функция', b'type']
for i in list:
    try:
        print(i)
    except SyntaxError:
        print('Слово не перевести в байты')

#Слова класс и функция вызовут ошибку из-за кириллицы

''' Задание № 4'''
list_words = ['разработка', 'администрирование', 'protocol', 'standard']
for i in list_words:
    print(i.encode('utf-8'), (i.encode('utf-8')).decode('utf-8'))


''' Задание № 5'''

youtube = ['ping', 'youtube.com']
yandex = ['ping', 'yandex.ru']

subproc_ping_youtube = subprocess.Popen(youtube, stdout=subprocess.PIPE)

for line in subproc_ping_youtube.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

subproc_ping_yandex = subprocess.Popen(yandex, stdout=subprocess.PIPE)

for line in subproc_ping_yandex.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

''' Задание № 6'''


with open('test_file.txt') as f_n:
    print(f'Кодировка файла - {locale.getpreferredencoding()}')
    for row in f_n:
        print((row.encode('cp1251')).decode('utf-8'))
