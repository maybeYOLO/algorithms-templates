from time import time

from broken_search import broken_search

time_start = time()
max_dimension = 10
count = 0
for list_length in range(1, max_dimension):
    for offset in range(list_length):
        nums = []
        for value in range(list_length):
            nums.append((value + offset) % list_length)
        for target in range(list_length + 1):
            result = -1 if target == list_length else (target - offset) % list_length
            res = broken_search(nums, target)
            count += 1
            if res != result:
                print(f'{target} {offset} {nums} {result, res}')
print(max_dimension, count, time() - time_start)
