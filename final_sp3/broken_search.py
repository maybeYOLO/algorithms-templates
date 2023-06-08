from typing import List


def broken_search(nums: List[int], target: int) -> int:

    def partial_search() -> int:

        nonlocal nums, target, left, right, left_value, right_value

        index = left + (right - left) // 2
        new_value = nums[index]
        if new_value == target:
            return index
        if left >= right - 1:
            return -1
        if left_value < target < new_value:
            right = index
            right_value = new_value
        elif new_value < target < right_value:
            left = index
            left_value = new_value
        elif left_value > new_value:
            right = index
            right_value = new_value
        else:
            left = index
            left_value = new_value
        return partial_search()

    left = 0
    left_value = nums[left]
    if left_value == target:
        return left
    right = len(nums) - 1
    right_value = nums[right]
    if right_value == target:
        return right
    return partial_search()


def test() -> None:
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
