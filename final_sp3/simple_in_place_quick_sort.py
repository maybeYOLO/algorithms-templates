def q_sort(nums, left, right, count) -> None:
    if left == right:
        return
    if right - left == 1:
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        return
    if count > 10:
        print('count limit')
        return
    count += 1
    start = left
    end = right
    pivot = nums[left]
    print(pivot, start, left, right, end, nums)
    while left < right:
        while nums[left] < pivot and left < right:
            left += 1
        while nums[right] >= pivot and left < right:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        print(pivot, start, left, right, end, nums, 's')
    print(pivot, start, left, right, end, nums, count)
    q_sort(nums, start, left, count)
    q_sort(nums, right, end, count)
    

nums = [4, 8, 9, 20, 1, 5, 3, 10]
q_sort(nums, 0, len(nums) - 1, 0)
print(nums)
