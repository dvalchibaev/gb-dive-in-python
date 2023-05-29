"""
✔ Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
import os, sys
from itertools import count
from string import ascii_letters
from random import choices, randint, randbytes


# создать функцию произвольной генерации файлов
def create_random_files(quantity: int = 1, ftype: str = 'test', target_dir: str | None = None,
                        min_len_name: int = 6, max_len_name: int = 30,
                        min_byte_size: int = 256, max_byte_size: int = 4096) -> None:
    if target_dir:
        if target_dir not in os.listdir():
            os.mkdir(target_dir)
        fdir = target_dir + '/'
    else:
        fdir = ''
    for _ in range(quantity):
        len_name = randint(min_len_name, max_len_name)
        file_name = fdir + ''.join(choices(ascii_letters, k=len_name)) + '.' + ftype
        fsize = randint(min_byte_size, max_byte_size)
        with open(file_name, 'wb') as f:
            f.write(randbytes(fsize))


def rename_files(type_to_edit: str, target_type: str,
                 name_strip: list[int], target_name: str = '',
                 series_length: int = 3, files_dir: str | None = None):
    i = count(start=0, step=1)
    cdir = f'{files_dir}/' if files_dir else ''
    print(f'Файлы в папке: {os.listdir(files_dir)}')
    for file in os.listdir(files_dir):
        fname, ftype = file.split('.')
        if ftype == type_to_edit:
            start = max(name_strip[0]-1, 0)
            finish = min(name_strip[-1]-1, len(fname))
            renamed_file = f'{file[start:finish]}{target_name}{get_series(series_length,next(i))}.{target_type}'
            print(f'Меняю название файла {file}', f'Результирующее название {renamed_file}')
            os.rename(f'{cdir}{file}', f'{cdir}{renamed_file}')


def get_series(series_length: int, number: int) -> str:
    return '0' * max(0, series_length - len(str(number))) + str(number)


create_random_files(quantity=4, target_dir='Test', ftype='ttt')
create_random_files(quantity=4, target_dir='Test', ftype='tst')
rename_files('tst', 'tts', [2, 8], files_dir='Test')
