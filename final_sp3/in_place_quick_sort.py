# ID = 

from typing import List, Tuple

NAME_INDEX = 0
SCORE_INDEX = 1
PENALTY_INDEX = 2


def _nums_gt(left_value: Tuple[str, int, int], right_value: Tuple[str, int, int]) -> bool:
    return left_value[SCORE_INDEX] < right_value[SCORE_INDEX] or (
        left_value[SCORE_INDEX] == right_value[SCORE_INDEX]
        and (left_value[PENALTY_INDEX] > right_value[PENALTY_INDEX] or (
            left_value[PENALTY_INDEX] == right_value[PENALTY_INDEX]
            and left_value[NAME_INDEX] > right_value[NAME_INDEX]
        ))
    )


def _q_sort(nums: List[Tuple[str, int, int]], left: int, right: int) -> None:
    if left == right:
        return
    if right - left == 1:
        if _nums_gt(nums[left], nums[right]):
            nums[left], nums[right] = nums[right], nums[left]
        return
    start = left
    end = right
    pivot = nums[left]
    while left < right:
        while _nums_gt(pivot, nums[left]) and left < right:
            left += 1
        while not _nums_gt(pivot, nums[right]) and right > left:
            right -= 1
        if left != right:
            nums[left], nums[right] = nums[right], nums[left]
    if left > start:
        _q_sort(nums, start, left - 1)
        _q_sort(nums, left, end)
    else:
        _q_sort(nums, left + 1, end)


def in_place_quick_sort(participants: List[Tuple[str, int, int]]) -> None:
    _q_sort(participants, 0, len(participants) - 1)


if __name__ == '__main__':
    participants = []
    entry_count = int(input())
    for _ in range(entry_count):
        name, tasks, penalty = input().strip().split()
        participants.append((name, int(tasks), int(penalty)))
    in_place_quick_sort(participants)
    print(' '.join(map(lambda el: el[0], participants)))
