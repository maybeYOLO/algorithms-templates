# ID 87201921

from typing import Tuple


def process_row(row: str, number: int):
    check = str(number)
    result = 0
    for symbol in row:
        if symbol == check:
            result += 1
    return result


def trainer(k: int, row1: str, row2: str, row3: str, row4: str) -> int:
    result = 0
    for number in range(1, 10):
        count = 0
        count += process_row(row1, number)
        count += process_row(row2, number)
        count += process_row(row3, number)
        count += process_row(row4, number)
        if count > 0 and count <= k * 2:
            result += 1
    return result


def read_input() -> Tuple[int, str, str, str, str]:
    k = int(input())
    row1 = input().strip()
    row2 = input().strip()
    row3 = input().strip()
    row4 = input().strip()
    return k, row1, row2, row3, row4


print(trainer(*read_input()))
