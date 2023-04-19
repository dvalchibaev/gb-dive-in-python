"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""


# Сумма пополнения и снятия кратны 50 у.е.
def sum_is_valid(m_sum:int) -> bool:
    if m_sum < 0 or m_sum % 50 != 0:
        print("Неверная сумма!")
        return False
    return True


# После каждой третей операции пополнения или снятия начисляются проценты - 3%
def gain_interest(account:dict) -> None:
    if len(account['operations']) % 3 == 0:
        interest = (0.03 * account['sum'])
        print(f"Начисление за обслуживание {interest:.2f}")
        account['sum'] += interest
        print(f"Баланс {account['sum']}")


# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
def large_sum_fee(account:dict) -> None:
    if account['sum'] >= 5_000_000:
        print(f'Предупреждение! Комиссия за большую сумму на счете'
              f'{0.1 * account["sum"]}')
        account['sum'] *= 0.9
        print(f"Баланс перед операцией {account['sum']}")


def manage_bank_account(account=None) -> dict:
    if account is None:
        account = {"sum": 0, "operations": []}
    while True:
        large_sum_fee(account)
        match input("Введите команду: 1. пополнить 2. снять 3. выйти \n :").lower():
            case 'пополнить': bank_account_top_up(account)
            case 'снять': bank_account_withdraw(account)
            case 'выйти': break
            case _: continue
    report = '\n'.join(account['operations'])
    print(f"Проведенные операции:\n {report} \nБаланс: {account['sum']}")
    return account


def bank_account_top_up(account:dict) -> bool:
    tu_sum = int(input("Введите сумму, кратную 50: "))
    if not sum_is_valid(tu_sum):
        return False
    account['sum'] += tu_sum
    bank_account_log(account, f"Пополнение на {tu_sum} у.е., ")
    gain_interest(account)
    return True


def bank_account_withdraw(account:dict) -> bool:
    w_sum = int(input("Введите сумму, кратную 50: "))
    if not sum_is_valid(w_sum):
        return False
    fee = 1.5 * w_sum // 100
    if fee > 600: fee = 600
    if fee < 30: fee = 30
    if w_sum + fee > account['sum']:
        print("Сумма больше, чем на счете!")
        return False
    account['sum'] -= (w_sum + fee)
    bank_account_log(account, f"Снятие {w_sum} у.е., комиссия {fee}")
    gain_interest(account)
    return True


# Дополнительно сохраняйте все операции поступления и снятия средств в список.
def bank_account_log(account:dict, log:str) -> bool:
    print(log, f"Баланс {account['sum']} у.е.")
    account['operations'].append(log)
    return True


manage_bank_account()