"""
Тимофей ищет место, чтобы построить себе дом.
Улица, на которой он хочет жить, имеет длину n,
то есть состоит из n одинаковых идущих подряд участков.
Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка.
Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы.
Дома в городе Тимофея нумеровались в том порядке, в котором строились,
поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.
"""

from typing import List

# В первой строке дана длина улицы —– n (1 ≤ n ≤ 10^6)
MAX_STREET_LENGTH = 1_000_000


def process_street(street) -> str:
    street_length = len(street)
    distances = [0] * street_length
    forward_count = MAX_STREET_LENGTH + 1
    fence = 0
    for index in range(street_length):
        if street[index] == 0:
            backward_count = 0
            back_index = index
            while back_index >= fence:
                distances[back_index] = min(distances[back_index], backward_count)
                backward_count += 1
                back_index -= 1
            fence = index
            forward_count = 1
        else:
            distances[index] = forward_count
            forward_count += 1
    return " ".join(map(str, distances))


def read_input() -> List[int]:
    _ = input()
    return list(map(int, input().strip().split()))


# print(process_street(read_input()))

print(process_street((0, 1, 4, 9, 0)))       # 0 1 2 1 0
print(process_street((0, 7, 9, 4, 8, 20)))   # 0 1 2 3 4 5
print(process_street((1, 2, 3, 4, 0)))       # 4 3 2 1 0
