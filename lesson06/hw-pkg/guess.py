'''
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
'''
from random import randrange
from sys import argv


def play_guess(l_bound: int = 0, u_bound: int = 100, guesses: int = 5) -> bool:
    goal = randrange(l_bound, u_bound)
    for _ in range(guesses):
        guess = int(input('Введите число: '))
        if guess == goal:
            print('Верно!')
            return True
        elif guess > goal:
            print('Меньше!')
        else:
            print('Больше!')
    return False


if __name__ == '__main__':
    args = [int(i) for i in argv[1:]]
    match len(args):
        case 1:
            play_guess(guesses=args[0])
        case 2:
            play_guess(l_bound=args[0], u_bound=args[1])
        case 3:
            play_guess(l_bound=args[0], u_bound=args[1], guesses=args[2])
        case _:
            print('Неверное количество аргументов!')
