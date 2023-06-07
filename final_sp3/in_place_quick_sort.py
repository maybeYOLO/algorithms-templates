# ID = 88016414

from typing import List, Union

NAME_INDEX = 0
SCORE_INDEX = 1
PENALTY_INDEX = 2


def nums_gt(left_value, right_value) -> bool:
    return left_value[SCORE_INDEX] < right_value[SCORE_INDEX] or (
        left_value[SCORE_INDEX] == right_value[SCORE_INDEX]
        and (left_value[PENALTY_INDEX] > right_value[PENALTY_INDEX] or (
            left_value[PENALTY_INDEX] == right_value[PENALTY_INDEX]
            and left_value[NAME_INDEX] > right_value[NAME_INDEX]
        ))
    )


def nums_ge(left_value, right_value) -> bool:
    return left_value[SCORE_INDEX] < right_value[SCORE_INDEX] or (
        left_value[SCORE_INDEX] == right_value[SCORE_INDEX]
        and (left_value[PENALTY_INDEX] > right_value[PENALTY_INDEX] or (
            left_value[PENALTY_INDEX] == right_value[PENALTY_INDEX]
            and left_value[NAME_INDEX] >= right_value[NAME_INDEX]
        ))
    )


def q_sort(nums, left, right) -> None:
    if left == right:
        return
    if right - left == 1:
        if nums_gt(nums[left], nums[right]):
            nums[left], nums[right] = nums[right], nums[left]
        return
    start = left
    end = right
    pivot = nums[left]
    while left < right:
        while nums_gt(pivot, nums[left]) and left < right:
            left += 1
        while nums_ge(nums[right], pivot) and right > left:
            right -= 1
        if nums_gt(nums[left], nums[right]):
            nums[left], nums[right] = nums[right], nums[left]
    if left > start:
        q_sort(nums, start, left - 1)
        q_sort(nums, left, end)
    else:
        q_sort(nums, left + 1, end)


def in_place_quick_sort(participants: List[List[Union[str, int]]]) -> None:
    q_sort(participants, 0, len(participants) - 1)


if __name__ == '__main__':
    participants = []
    entry_count = int(input())
    for _ in range(entry_count):
        name, tasks, penalty = input().strip().split()
        participants.append([name, int(tasks), int(penalty)])
    in_place_quick_sort(participants)
    for participant in participants:
        print(participant[0])
