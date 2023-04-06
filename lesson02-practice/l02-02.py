"""Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег"""
SUM = 0
OPERATION_COUNT = 0


def control():
    a = int(input('Выберите: 1. Пополнить 2. Снять 3. Выйти\n'))
    return a


def deposit() -> None:
    global SUM, OPERATION_COUNT
    if SUM > 5_000_000:
        SUM *= 0.9
    OPERATION_COUNT += 1
    amount = int(input('Введите сумму кратную 50\n'))
    if amount % 50 == 0:
        SUM += amount
    else:
        while amount % 50:
            amount = int(input('Введите сумму кратную 50\n'))
        SUM += amount
    if OPERATION_COUNT % 3 == 0:
        SUM *= 1.03
    print(f'Сумма на счете равна {SUM}')


# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
def cashout():
    global SUM
    if SUM > 5_000_000:
        SUM *= 0.9
    amount = int(input('Введите сумму снятия кратную 50\n'))
    if amount % 50 != 0:
        while amount % 50:
            amount = int(input('Введите сумму кратную 50\n'))
    interest = 1.5 * amount / 100
    if interest < 30:
        interest = 30
    if interest > 600:
        interest = 600
    if SUM >= amount + interest:
        SUM -= amount + interest
    else:
        print('Недостаточно средств на счете')
    if OPERATION_COUNT % 3 == 0:
        SUM *= 1.03
    print(f'Сумма на счете равна {SUM}')


command = control()
while command != 3:
    match command:
        case 1: deposit()
        case 2: cashout()
        case _: break
    command = control()
