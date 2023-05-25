"""
Напишите функцию для транспонирования матрицы
"""


def transpose_matrix(matrix:list[list[float]]) -> list[list[float]]:
    result = [[matrix[j][i]
              for j in range(len(matrix))]
              for i in range(len(matrix[0]))]
    return result


def print_matrix(matrix:list) -> None:
    for i in range(len(matrix)):
        print(*matrix[i])

matr = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print("Исходная матрица:")
print_matrix(matr)
print("Транспонированная матрица:")
print_matrix(transpose_matrix(matr))