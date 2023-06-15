"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
"""

import math, fractions

fraction1 = [int(x) for x in input("Введите первую дробь в формате a/b: ").split('/')]
fraction2 = [int(x) for x in input("Введите вторую дробь в формате a/b: ").split('/')]
fr1 = fractions.Fraction(*fraction1)
fr2 = fractions.Fraction(*fraction2)

lcm = math.lcm(fraction1[-1], fraction2[-1])
frac_sum = [
    fraction1[0] * lcm // fraction1[-1] + fraction2[0] * lcm // fraction2[-1],
    lcm
]
frac_mult = [fraction1[0] * fraction2[0], fraction1[-1] * fraction2[-1]]
for frac in (frac_mult, frac_sum):
    gcd = math.gcd(*frac)
    frac[0] = frac[0] // gcd
    frac[-1] = frac[-1] //gcd

print(f'Сумма: {frac_sum[0]}/{frac_sum[-1]}', f'Проверка через fractions: {fr1 + fr2}')
print(f'Произведение: {frac_mult[0]}/{frac_mult[-1]}', f'Проверка через fractions: {fr1 * fr2}')