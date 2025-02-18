from typing import List, Tuple


""""Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.

Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7."""

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    max_row = len(matrix) - 1
    max_col = len(matrix[0]) - 1
    if col + 1 <= max_col:
        result.append(matrix[row][col + 1])
    if col - 1 >= 0:
        result.append(matrix[row][col - 1])
    if row + 1 <= max_row:
        result.append(matrix[row + 1][col])
    if row - 1 >= 0:
        result.append(matrix[row - 1][col])
    result.sort()
    return result

def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
