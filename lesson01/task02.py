# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

NON_PRIME = "не простое"
PRIME = "число простое"

while True:
    prime_candidate = int(input("Введите неотрицательное число не больше 100 000\n"))
    if not (0 <= prime_candidate <= 100_000):
        print("некорректный ввод\n")
        continue
    if prime_candidate in (2, 3, 5, 7):
        is_prime = True
    elif prime_candidate < 2 or prime_candidate % 2 == 0:
        is_prime = False
    else:
        is_prime = True
        for i in range(3, int(prime_candidate ** 0.5 + 1), 2):
            if prime_candidate % i == 0:
                is_prime = False
    print(PRIME) if is_prime else print(NON_PRIME)
    break