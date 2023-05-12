"""
Игра «Тренажёр для скоростной печати» представляет собой поле из клавиш 4x4.
В нём на каждом раунде появляется конфигурация цифр и точек.
На клавише написана либо точка, либо цифра от 1 до 9.

В момент времени t игрок должен одновременно нажать на все клавиши,
на которых написана цифра t.
Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый.
Если в момент времени t нажаты все нужные клавиши, то игроки получают 1 балл.

Найдите число баллов, которое смогут заработать Гоша и Тимофей,
если будут нажимать на клавиши вдвоём.
"""

from typing import Tuple, List


def process_row(row: str, num_sum: List[int]) -> None:
    for index in range(1, 10):
        for sym in row:
            if sym == str(index):
                num_sum[index - 1] += 1


def trainer(k: int, row1: str, row2: str, row3: str, row4: str) -> int:
    result = 0
    num_sum = [0] * 9
    process_row(row1, num_sum)
    process_row(row2, num_sum)
    process_row(row3, num_sum)
    process_row(row4, num_sum)
    for n_sum in num_sum:
        if 0 < n_sum <= k * 2:
            result += 1
    return result


def read_input() -> Tuple[int, str, str, str, str]:
    k = int(input())
    row1 = input().strip()
    row2 = input().strip()
    row3 = input().strip()
    row4 = input().strip()
    return k, row1, row2, row3, row4


# print(trainer(read_input())

print(trainer(3, '1231', '2..2', '2..2', '2..2'))   # 2
print(trainer(4, '1111', '9999', '1111', '9911'))   # 1
print(trainer(4, '1111', '1111', '1111', '1111'))   # 0
