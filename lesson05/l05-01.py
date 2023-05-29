"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""
PATH_TO_FILE = '/home/alchibaevdv/PycharmProjects/GB_Intro_Python/gb-dive-in-python/lesson05/l05-03.py'


def parse_file_path(file_path: str):
    *path, file = file_path.split('/')
    name, extention = file.split('.')
    return '/'.join(path), name, extention


path, name, extention = parse_file_path(PATH_TO_FILE)
print(f'{path=}, {name=}, {extention=}')