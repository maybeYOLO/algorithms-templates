# utf-8
from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    max_length = len(temperatures)
    for i in range(max_length):
        if i == 0:
            previous = True
        else:
            previous = temperatures[i] > temperatures[i - 1]
        if i == max_length - 1:
            next = True
        else:
            next = temperatures[i] > temperatures[i + 1]
        if previous and next:
            count += 1
    return count


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures

temperatures = read_input()
print(get_weather_randomness(temperatures))
