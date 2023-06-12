'''Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами отрицательной длины.'''


class NonQuadraticException(ValueError):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return "Ошибка: не кважратное уравнение"


class ZeroRootsError(ArithmeticError):

    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return "Ошибка: Нет вещественных корней!"


def quadratic_roots(a: float, b: float, c: float) -> tuple:
    """Нахождение корней квадратного уравнения"""
    if a == 0:
        raise NonQuadraticException
    det = b * b - 4 * a * c
    if det < 0:
        raise ArithmeticError("Нет вещественных корней")
    try:
        result = 0.5 * (-b - det ** 0.5) / a, 0.5 * (-b + det ** 0.5) / a
        return result
    except ValueError as err:
        raise err
    except ZeroDivisionError as div_by_zero:
        raise div_by_zero


# quadratic_roots(0, 1, -1)
quadratic_roots(1, 0, 1)