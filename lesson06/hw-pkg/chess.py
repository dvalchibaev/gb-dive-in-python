'''
2. Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
3. Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''
from sys import argv
from random import randint

PIECES = [i + j for i in ['W', 'B'] for j in ['K', 'Q', 'R', 'B', 'N', 'p']]
CHESS = {item: ' ' + chr(9812 + i) + ' ' for i, item in enumerate(PIECES)}


# решение задачи 2
def eight_queens(queens: list[list[int]]) -> bool:
    for queen in queens:
        q1, q2 = queen
        for i in range(1, 9):
            for p in (-1, 1):
                if [q1, q2 + p * i] in queens or [q1 + p * i, q2] in queens:
                    return False
                if [q1 + p * i, q2 + p * i] in queens or [q1 - p * i, q2 + p * i] in queens:
                    return False
    return True


def get_random_chess(n: int = 8) -> list[list[int]]:
    # произвольно расположенные ферзи
    return [[i, randint(1, 8)] for i in range(1, 9)]


# решение задачи 3
def eight_queens_solver():
    count = 4
    result = []
    while count > 0:
        sets = get_random_chess(8)
        if eight_queens(sets) and sets not in result:
            result.append(sets)
            brd = new_board()
            set_board(brd, sets)
            print_board(brd)
            count -= 1


def chess_square(i: int) -> str:
    # рисует белый или черный квадрат
    if i == 0:
        return chr(9617) * 3
    return chr(9608) * 3


def new_board() -> list[list[str]]:
    # пустая доска для отрисовки
    return [[chess_square((i + j) % 2) for i in range(8)] for j in range(8)]


def set_board(board: list[list[str]], pieces: list[list[int]]) -> list[list[str]]:
    # заполняем шахматную доску фигурами(пока только ферзями)
    if board is None:
        board = new_board()
    if pieces is None:
        pass
    for i in pieces:
        set_piece(i, 'WQ', board)
    return board


def print_board(board: list[list[str]]) -> None:
    # отображает шахматную доску
    AXIS_X = '  ' + '  '.join(list('ABCDEFGH')) + '  '
    AXIS_Y = '87654321'
    draw = '\n'.join([AXIS_Y[i] + ''.join(board[i]) + AXIS_Y[i] for i in range(len(board))]) + '\n'
    print(AXIS_X + '\n' + draw + AXIS_X)
    pass


def set_piece(place: list[int], figure: str,
              board: list[list[str]] = None) -> bool:
    # добавляет фигуру (ферзя) на шахматное поле
    if figure not in CHESS:
        return False
    if place[0] not in range(1, 9) or place[1] not in range(1, 9):
        return False
    if board is None:
        board = new_board()
    board[8 - place[0]][place[1] - 1] = CHESS[figure]
    return True


if __name__ == '__main__':
    _, *parameters = argv
    print('4 решения задачи 8 ферзей:')
    eight_queens_solver()
    print('Успех!!!')
