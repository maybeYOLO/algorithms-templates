# ID = 87455478

from typing import List


def process_between_zeros(
    start: int,
    finish: int,
    distance: List[int]
) -> None:
    count = 1
    delta = 1
    middle = start + (finish - start - 1) / 2
    for index in range(start + 1, finish):
        distance[index] = count
        if index == middle:
            delta = 0
        elif index > middle:
            delta = -1
        count += delta


def process_street(street: List[str]) -> str:
    street_length = len(street)
    distance = [0] * street_length
    zero_met = False
    start = 0
    for index in range(street_length):
        if street[index] == "0":
            if zero_met:
                process_between_zeros(start, index, distance)
            else:
                for distance_index in range(index):
                    distance[distance_index] = index - distance_index
                zero_met = True
            start = index
    if start < street_length:
        for index in range(start + 1, street_length):
            distance[index] = index - start
    return " ".join(map(str, distance))


if __name__ == '__main__':


    def read_input() -> List[str]:
        _ = input()
        return input().strip().split()


    print(process_street(read_input()))
