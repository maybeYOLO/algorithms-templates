# ID 87455588

from typing import Tuple, List

NUM_PLAYERS = 2


def trainer(key_limit: int, matrix: List[str]) -> int:
    counts = dict()
    for row in matrix:
        for symbol in row:
            if symbol != '.':
                if symbol in counts:
                    counts[symbol] += 1
                else:
                    counts[symbol] = 1
    return sum(1 if 0 < counts[x] <= key_limit else 0 for x in counts)


if __name__ == '__main__':


    def read_input() -> Tuple[int, List[str]]:
        keys = int(input())
        matrix = []
        for _ in range(4):
            matrix.append(input().strip())
        return keys * NUM_PLAYERS, matrix

    print(trainer(*read_input()))
