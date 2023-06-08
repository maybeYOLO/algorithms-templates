from simple_broken_search import broken_search

assert broken_search([5, 1], 1) == 1

for list_length in range(1, 6):
    for offset in range(list_length):
        nums = []
        for value in range(list_length):
            nums.append((value + offset) % list_length)
        print(nums)
