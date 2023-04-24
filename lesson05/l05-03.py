"""Создайте функцию генератор чисел Фибоначчи"""


def yield_fibonacci():
    num1, num2 = 0, 1
    while True:
        num1, num2 = num2, num2 + num1
        yield num1


fib = yield_fibonacci()
for _ in range(10):
    print(next(fib))