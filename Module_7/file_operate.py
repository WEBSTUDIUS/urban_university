import os
import time


def print_file(file, filepath):
    filetime = os.stat(filepath).st_mtime
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.stat(filepath).st_size
    parent_dir = os.path.dirname(filepath)
    print(
        f'Обнаружен файл: {file}, '
        f'Путь: {filepath}, '
        f'Размер: {filesize} байт, '
        f'Время изменения: {formatted_time}, '
        f'Родительская директория: {parent_dir}')


def is_file(item_cat, path=os.getcwd()):
    filepath = os.path.join(path, item_cat)
    if not os.path.exists(filepath):
        return False
    if os.path.isfile(filepath):
        print_file(item_cat, filepath)
    else:
        for item in os.listdir(filepath):
            is_file(item, filepath)


directory = '.'
for dirs in os.walk(directory):
    for dir_ in dirs:
        if not isinstance(dir_, str):
            for item in dir_:
                is_file(item)
