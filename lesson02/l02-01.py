"""
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
HEXES = '0123456789abcdef'


to_hex = int(input("Введите число для преобразования в шестнадцатиричное: "))
hexed_number = ''
base = 16
iter_n = to_hex

while iter_n:
    hexed_number += HEXES[iter_n % base]
    iter_n //= base
hexed_number = '0x' + hexed_number[::-1]
print(hexed_number, hex(to_hex))