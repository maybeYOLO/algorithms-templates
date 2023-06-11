# ID = 88040814

from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Participant:
    name: str
    score: int
    penalty: int

    def __gt__(self, other):
        return (
            self.score < other.score
            or (self.score == other.score
                and (self.penalty > other.penalty
                or (self.penalty == other.penalty
                    and self.name > other.name
                    ))
                ))


def in_place_quick_sort(nums: List[Participant]) -> None:

    def q_sort(left: int, right: int) -> None:

        nonlocal nums

        if left == right:
            return
        if right - left == 1:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
            return
        start = left
        end = right
        pivot = nums[left]
        while left < right:
            while pivot > nums[left] and left < right:
                left += 1
            while not pivot > nums[right] and right > left:
                right -= 1
            if left != right:
                nums[left], nums[right] = nums[right], nums[left]
        if left > start:
            q_sort(start, left - 1)
            q_sort(left, end)
        else:
            q_sort(left + 1, end)

    q_sort(0, len(nums) - 1)


if __name__ == '__main__':
    participants: List[Participant] = []
    entry_count = int(input())
    for _ in range(entry_count):
        name, tasks, penalty = input().strip().split()
        participants.append(Participant(name, int(tasks), int(penalty)))
    in_place_quick_sort(participants)
    print('\n'.join(map(lambda el: el.name, participants)))
