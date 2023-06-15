"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

test_data = [1, 2, 3, 4, 1, -5, 3, -5, 2, 7, 100, 1, 0, 3, 3, 3]

dups = dict()
for item in test_data:
    if dups.get(item):
        dups[item] += 1
    else:
        dups[item] = 1
duplicates = [item for item in test_data if dups[item] == 2]
print(f'{test_data = }, {duplicates = }')