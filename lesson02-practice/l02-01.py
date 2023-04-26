# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.
import sys
data = [3, 4.5, 'word', 4, False, 'word', 3, '3']


for i, elem in enumerate(data, 1):
    print(f'{i}, {elem =}, {id(elem)}, {sys.getsizeof(elem)}, {hash(elem)}, '
          f'{True if isinstance(elem,int) else ""}, {True if isinstance(elem, str) else ""}')
#
#
# data2 = data[::].append(data[::])
#
#
# for i, elem in enumerate(data2, 1):
#     print(f'{i}, {elem}, {id(elem)}, {sys.getsizeof(elem)}, {hash(elem)}, '
#           f'{True if isinstance(elem,int) else ""}, {True if isinstance(elem, str) else ""}')
