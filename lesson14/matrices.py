


class Matrix:
    def __init__(self, elems: list[list]):
        self.elements = elems
        self.rows = len(elems)
        self.columns = len(elems[0])

    def comparable(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return False
        return True

    def __str__(self):
        return '\n'.join((' '.join((str(x) for x in self.elements[i]))
                          for i in range(len(self.elements)))) + '\n'

    def __add__(self, other):
        if not self.comparable(other):
            print("Матрицы разных размеров")
            return None
        result = [[(self.elements[i])[j] + other.elements[i][j]
                   for j in range(self.columns)]
                  for i in range(self.rows)]
        return Matrix(result)

    def __eq__(self, other):
        if not self.comparable(other):
            return False
        for i in range(self.rows):
            for j in range(self.columns):
                if self.elements[i][j] != other.elements[i][j]:
                    return False
        return True

    def __ne__(self, other):
        if self == other:
            return False
        return True


A = Matrix([[1, 2, 3], [4, 5, 6]])
print(A, f'A != A + A: \n {A != A + A}')
