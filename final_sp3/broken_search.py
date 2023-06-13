# ID = 

from typing import List


def broken_search(nums: List[int], target: int) -> int:

    left_index = 0
    if nums[left_index] == target:
        return left_index
    right_index = len(nums) - 1
    if nums[right_index] == target:
        return right_index

    while left_index < right_index - 1:
        middle_index = left_index + (right_index - left_index) // 2
        middle_value = nums[middle_index]
        if middle_value == target:
            return middle_index
        if nums[left_index] < target < middle_value:
            right_index = middle_index
        elif middle_value < target < nums[right_index]:
            left_index = middle_index
        elif nums[left_index] > middle_value:
            right_index = middle_index
        else:
            left_index = middle_index
    return -1


if __name__ == '__main__':
    def test() -> None:
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr, 5) == 6
