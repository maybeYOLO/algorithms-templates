from typing import List


def partial_search(nums: List[int], target: int, index: int, half_length: int, full_length: int) -> int:
    if nums[index] == target:
        return index
    if half_length == 10:
        return -1
    return partial_search(nums, target, (index + 1) % full_length, half_length, full_length)


def broken_search(nums: List[int], target: int) -> int:
    return partial_search(nums, target, 0, len(nums) // 2, len(nums))


def test() -> None:
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
