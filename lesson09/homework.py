# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.


import csv, json
from random import randint
from typing import Callable


COEFFICIENTS_LIMIT = 100
CSV_FILE = 'quadratics.csv'
JSON_FILE = 'test.json'


def mass_solver(file: str):
    def deco(func: Callable) -> Callable:
        cache = {}

        def wrapper(*args, **kwargs):
            with open(file, 'r') as f:
                csv_file = csv.reader(f)
                for line in csv_file:
                    a, b, c = (int(x) for x in line)
                    key = ', '.join(line)
                    cache[key] = func(a, b, c)
            return cache
        return wrapper
    return deco


def export_json(dump_file: str):
    def deco(fun: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = fun(*args, **kwargs)
            json.dump(result, open(dump_file, 'w+', encoding='utf-8'))
            return result
        return wrapper
    return deco


@export_json(JSON_FILE)
@mass_solver(CSV_FILE)
def quadratic_roots(a: float, b: float, c: float) -> tuple | None:
    """Нахождение корней квадратного уравнения"""
    if a == 0:
        return None
    det = b * b - 4 * a * c
    if det < 0:
        return None
    return 0.5 * (-b - det ** 0.5) / a, 0.5 * (-b + det ** 0.5) / a


def create_csv(file: str = CSV_FILE,
               lines: int = 100, limit: int = COEFFICIENTS_LIMIT) -> bool:
    with open(f'{file}', 'w+', newline='\n') as f:
        csv_file = csv.writer(f, dialect='excel')
        data = ((randint(-limit, limit) for _ in range(3)) for _ in range(lines))
        csv_file.writerows(data)
    return True


print(quadratic_roots())
