from typing import List
import logging


def partial_search(nums: List[int], target: int, index: int, half_length: int, full_length: int) -> int:
    logging.info(f'\'{target}\' {index, nums[index]} {nums} {half_length}')
    if nums[index] == target:
        return index
    if half_length == 0:
        return -1
    if nums[index] > target:
        new_index = (index - half_length) % full_length
    else:
        new_index = (index + half_length) % full_length
    half_length //= 2
    logging.info(f'nums[index] > target \'{nums[index] > target}\' {new_index, nums[new_index]} {nums} {half_length}')
    return partial_search(nums, target, new_index, half_length, full_length)


def broken_search(nums: List[int], target: int) -> int:
    logging.warning('.' * 60)
    return partial_search(nums, target, 0, len(nums) // 2 * 2, len(nums))


logging.basicConfig(
    level=logging.DEBUG,
    filename="b_search.log",
    filemode="w",
    format="[%(levelname)s]\t%(message)s"
)

if __name__ == '__main__':
    print('Пример 1. Ожидается 6')
    print(broken_search(
        [19, 21, 100, 101, 1, 4, 5, 7, 12],
        5
    ))

    print('Пример 2. Ожидается 1')
    print(broken_search(
        [5, 1],
        1
    ))
