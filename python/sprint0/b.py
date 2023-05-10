from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    i = []
    for a, b in zip(a, b):
        i.append(a)
        i.append(b)
    return i

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
