'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''


def make_variables_dict(**kwargs) -> dict:
    result = dict()
    for item in kwargs:
        try:
            hash(kwargs[item])
        except TypeError:
            result[str(kwargs[item])] = item
        else:
            result[kwargs[item]] = item
    return result


print(make_variables_dict(a=1, b='s', c=[1, 2, 3]))