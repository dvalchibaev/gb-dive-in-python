'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''
from sys import argv


def check_date(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if not 1 <= year <= 9999:
        return False
    if month not in range(1, 13):
        return False
    if month in (1, 3, 5, 7, 8, 10, 12):
        return day in range(1, 31 + 1)
    if month in (4, 6, 9, 11):
        return day in range(1, 30 + 1)
    if month == 2:
        return day in range(1, 28 + 1 + leap_year(year))
    return False


def leap_year(year:int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == '__main__':
    name, *args = argv
    if args:
        print(check_date(args[0]))
