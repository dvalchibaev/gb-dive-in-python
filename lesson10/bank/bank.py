'''
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
'''


def sum_is_valid(m_sum:int) -> bool:
    if m_sum < 0 or m_sum % 50 != 0:
        print("Неверная сумма!")
        return False
    return True


class BankAccount:

    def __init__(self, initial_sum: int = 0):
        self.__account = initial_sum
        self.__operation_tick = 0
        self.__operation_count = 0
        self.__interest_rate = 1.03

    def start_interaction(self):
        self.__ui()

    def __ui(self):
        MESSAGE: str = "Введите номер команды:\n" \
                    "1 (Пополнить счет)\n" \
                    "2 (Снять со счета)\n" \
                    "3 (Выйти)\n"
        while self.__controller(command=input(MESSAGE)):
            continue
        print("Завершение работы")

    def __controller(self, command: str = None) -> bool:
        self.__operation_tick += 1
        match command:
            case "1":
                self.__top_up()
                self.__operation_count += 1
                self.__info()
            case "2":
                self.__withdraw()
                self.__operation_count += 1
                self.__info()
            case "3":
                return False
            case _:
                print("Неверная комманда")
                self.__info()
        self.__gain_interest()
        self.__do_tax()
        return True

    def __top_up(self):
        while True:
            income = int(input("Введите сумму пополения\n"))
            if sum_is_valid(income):
                self.__account += income
                break

    def __withdraw(self):
        while True:
            withdraw = int(input("Введите сумму снятия\n"))
            if self.__account < withdraw:
                print("Сумма снятия больше суммы на счете!")
                continue
            elif sum_is_valid(withdraw):
                self.__account -= withdraw
                break

    def __gain_interest(self):
        if self.__operation_count % 3 == 0:
            self.__account *= self.__interest_rate

    def __do_tax(self):
        if self.__operation_tick == 3:
            if self.__account > 5_000_000:
                self.__account *= 0.9
            self.__operation_tick = 0

    def __info(self):
        print(f'Сумма на счете: {self.__account:2f}')


if __name__ == "__main__":
    account = BankAccount()
    account.start_interaction()