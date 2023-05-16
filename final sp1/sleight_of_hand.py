# ID 87374910

from typing import Tuple, List

NUM_PLAYERS = 2


def trainer(key_limit: int, matrix: List[str]) -> int:
    result = 0
    symbol_count = [0] * 9
    for row in matrix:
        for symbol in row:
            for check in range(1, 10):
                if symbol == str(check):
                    symbol_count[check - 1] += 1
    for count in symbol_count:
        if count > 0 and count <= key_limit:
            result += 1
    return result


def read_input() -> Tuple[int, List[str]]:
    keys = int(input())
    matrix = []
    for _ in range(4):
        matrix.append(input().strip())
    return keys * NUM_PLAYERS, matrix


if __name__ == '__main__':
    print(trainer(*read_input()))
