# ID = 87374855

from typing import List


def process_part(
    start: int,
    finish: int,
    zero_start: bool,
    zero_finish: bool,
    distance: List[int]
) -> None:
    """
    Обработка участка улицы от start до finish.
    zero_start - был ли пустой дом в начале участка
    zero_finish - был ли пустой дом в конце участка
    В случае если не было пустого дома в начале участка:
    дистанция будет уменьшаться.
    Если участок начинается и заканчивается пустым домом:
    дистанция сначала увеличивается, затем уменьшается.
    В случае если не было пустого дома в конце участка:
    дистанция будет увеличиваться.
    """

    if not zero_start:
        index = start
        count = finish - start
        while index < finish:
            distance[index] = count
            count -= 1
            index += 1
    elif zero_finish:
        index = start + 1
        count = 1
        delta = 1
        middle = start + (finish - start - 1) / 2
        while index < finish:
            distance[index] = count
            if index == middle:
                delta = 0
            elif index > middle:
                delta = -1
            count += delta
            index += 1
    else:
        index = start + 1
        count = 1
        while index <= finish:
            distance[index] = count
            count += 1
            index += 1


def process_street(street: List[str]) -> str:
    start = 0
    street_length = len(street)
    distance = [0] * street_length
    zero_met = False
    for index in range(street_length):
        if street[index] == "0":
            process_part(start, index, zero_met, True, distance)
            start = index
            zero_met = True
    if start < street_length:
        process_part(start, street_length - 1, zero_met, False, distance)
    return " ".join(map(str, distance))


def read_input() -> List[str]:
    _ = input()
    return input().strip().split()


if __name__ == '__main__':
    print(process_street(read_input()))
