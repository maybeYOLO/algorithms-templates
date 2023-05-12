# ID = 87200963

from typing import List


def process_street(street) -> str:
    zero_position = 0
    street_length = len(street)
    distance = [0] * street_length
    forward_count = 1_000_001
    for index in range(street_length):
        if street[index] == 0:
            reverse_index = index
            reverse_count = 0
            while reverse_index >= zero_position:
                if distance[reverse_index] > reverse_count:
                    distance[reverse_index] = reverse_count
                reverse_count += 1
                reverse_index -= 1
            zero_position = index
            forward_count = 1
        else:
            distance[index] = forward_count
            forward_count += 1
    return " ".join(map(str, distance))


def read_input() -> List[int]:
    _ = input()
    return list(map(int, input().strip().split()))


print(process_street(read_input()))
