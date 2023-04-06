# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1_000
num = randint(LOWER_LIMIT, UPPER_LIMIT)


for _ in range(10):
    guess = int(input('Введите число\n'))
    if num == guess:
        print('Верно!')
        break
    elif num > guess:
        print('Больше!')
    else:
        print('Меньше!')
else:
    print('Закончились попытки!')
