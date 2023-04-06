a = int(input("Введите a\n"))
b = int(input("Введите b\n"))
c = int(input("Введите c\n"))

d = b ** 2 - 4 * a * c
x1 = (-b - d ** 0.5) / 2 * a
x2 = (-b + d ** 0.5) / 2 * a
print(f'Полученные параметры: {a = }, {b = }, {c = }, {d = }, {x1 = }, {x2 = }')
