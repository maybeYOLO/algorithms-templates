from typing import List,Union


def in_place_quick_sort(participants: List[List[Union[str, int]]]) -> None:
    pass


if __name__ == '__main__':
    participants = []
    entry_count = int(input())
    for _ in range(entry_count):
        name, tasks, penalty = input().strip().split()
        participants.append([name, int(tasks), int(penalty)])
    in_place_quick_sort(participants)
    for participant in participants:
        print(participant[0])
