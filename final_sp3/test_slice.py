arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0
full_length = len(arr)
half_length = full_length // 2

# print(arr[index:half_length])
# print(arr[index:half_length:-1])
# print(arr[-1:])

print((index - half_length) % full_length)
print((index + half_length) % full_length)
