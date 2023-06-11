# ID = 

from typing import List
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

    def __lt__(self, other):
        return (
            self.score > other.score
            or (self.score == other.score
                and (self.penalty < other.penalty
                or (self.penalty == other.penalty
                    and self.name < other.name
                    ))
                ))


def partition(nums: List[Participant], left: int, right: int) -> int:
    pivot = nums[left + (right - left) // 2]
    while True:
        while nums[left] < pivot:
            left += 1
        while nums[right] > pivot:
            right -= 1
        if left >= right:
            return right
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


def quicksort(nums: List[Participant], left: int, right: int) -> None:
    if left >= 0 and right >= 0 and left < right:
        p = partition(nums, left, right)
        quicksort(nums, left, p)
        quicksort(nums, p + 1, right)


def in_place_quick_sort(nums: List[Participant]) -> None:
    quicksort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    participants: List[Participant] = []
    entry_count = int(input())
    for _ in range(entry_count):
        name, tasks, penalty = input().strip().split()
        participants.append(Participant(name, int(tasks), int(penalty)))
    in_place_quick_sort(participants)
    print('\n'.join(map(lambda el: el.name, participants)))
