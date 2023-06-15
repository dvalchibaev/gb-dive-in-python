# Возьмите любые 1-3 задачи из прошлых домашних заданий. # Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из # командной строки с передачей параметров
import logging
import argparse


logging.basicConfig(filename='lesson15.log',
                    filemode='w',
                    encoding='utf-8',
                    style='{',
                    level=logging.INFO,
                    #format='{asctime} {levelname:<8} функция {funcname}() строка {lineno:>3} : {msg}'
                    )
logger = logging.getLogger(__name__)


def input_matrix(n, m):
    matrix = []
    for _ in range(n):
        input_line = input()
        row = [float(i) for i in input_line.split()]
        if len(row) != m:
            msg = f'Неверный ввод матрицы: строка {row} не соответствует заявленной длине {m}'
            logger.error(msg)
            raise ImportError(msg)
        matrix.append(row)
    return Matrix(matrix)


def matrix_controller(command, *args):
    if len(args) != 4:
        MSG = f'Неверное количество аргументов ({len(args)} != 4)'
        logger.error(MSG)
        raise ImportError(MSG)
    n1, m1, n2, m2 = args
    match command:
        case 'add':
            A = input_matrix(n1, m1)
            B = input_matrix(n2, m2)
            logger.info(f'{A}\n{B}\n{A+B}')
            return A + B
        case '-eq':
            A = input_matrix(n1, m1)
            B = input_matrix(n2, m2)
            logger.info(f'{A}\n{B}\n{A == B}')
            return A == B
        case 'ne':
            A = input_matrix(n1, m1)
            B = input_matrix(n2, m2)
            logger.info(f'{A}\n{B}\n{A != B}')
            return A == B
        case _:
            MSG = f'Неверная команда {command}'
            logger.error(MSG)
            raise ValueError(MSG)


class Matrix:
    def __init__(self, elems: list[list]):
        self.elements = elems
        self.rows = len(elems)
        self.columns = len(elems[0])

    def comparable(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return False
        return True

    def __str__(self):
        return '\n'.join((' '.join((str(x) for x in self.elements[i]))
                          for i in range(len(self.elements)))) + '\n'

    def __repr__(self):
        return ','.join(str(row) for row in self.elements)

    def __add__(self, other):
        if not self.comparable(other):
            raise ValueError("Матрицы разных размеров")
        result = [[(self.elements[i])[j] + other.elements[i][j]
                   for j in range(self.columns)]
                  for i in range(self.rows)]
        return Matrix(result)

    def __eq__(self, other):
        if not self.comparable(other):
            raise ValueError("Матрицы разных размеров")
        for i in range(self.rows):
            for j in range(self.columns):
                if self.elements[i][j] != other.elements[i][j]:
                    return False
        return True

    def __ne__(self, other):
        if self == other:
            return False
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Совершить действия с матрицей')
    parser.add_argument('-add', type=int, nargs=4, help='Выполнить сложение матриц n1 x m1 и n2 x m2')
    parser.add_argument('-eq', type=int, nargs=4, help='Выполнить сравнение матриц n1 x m1 и n2 x m2')
    parser.add_argument('-ne', type=int, nargs=4, help='Выполнить сравнение матриц n1 x m1 и n2 x m2')
    args = parser.parse_args()
    if args.add:
        result = matrix_controller('add', *args.add)
        MSG = str(f'Выполняю сложение A+B:\n {result}')
        logger.info(msg=MSG)
    if args.eq:
        result = matrix_controller('eq', *args.eq)
        MSG = f'Выполняю сравнение A==B:\n {result}'
        logger.info(MSG)
    if args.ne:
        result = matrix_controller('ne', *args.ne)
        MSG = f'Выполняю сравнение A!=B:\n {result}'
        logger.info(MSG)
