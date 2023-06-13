from typing import List
import logging

def broken_search(nums: List[int], target: int) -> int:

    left_index = 0
    right_index = len(nums) - 1
    while left_index < right_index + 1:
        if nums[left_index] == target:
            return left_index
        if nums[right_index] == target:
            return right_index
        middle_index = left_index + (right_index - left_index) // 2
        middle_value = nums[middle_index]
        logging.info(f'\'{target}\' index {middle_index, middle_value} {nums} {left_index, right_index} {nums[left_index:right_index + 1]}')
        if middle_value == target:
            return middle_index
        if nums[left_index] < target < middle_value:
            right_index = middle_index - 1
        elif middle_value < target < nums[right_index]:
            left_index = middle_index + 1
        elif nums[left_index] > middle_value:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1
    return -1


def broken_search0(nums: List[int], target: int) -> int:

    def partial_search() -> int:

        nonlocal nums, target, left, right, left_value, right_value

        index = left + (right - left) // 2
        new_value = nums[index]
        logging.info(f'\'{target}\' index {index, new_value} {nums} {left, right} {nums[left:right + 1]}')
        if new_value == target:
            return index
        if left >= right - 1:
            return -1
        if left_value < target < new_value:
            logging.info('(1) plain left')
            right = index
            right_value = new_value
        elif new_value < target < right_value:
            logging.info('(2) plain right')
            left = index
            left_value = new_value
        elif left_value > new_value:
            logging.info('(3) anomaly left')
            right = index
            right_value = new_value
        else:
            logging.info('(4) anomaly right')
            left = index
            left_value = new_value
        return partial_search()

    logging.warning('.' * 60)
    left = 0
    left_value = nums[left]
    if left_value == target:
        return left
    right = len(nums) - 1
    right_value = nums[right]
    if right_value == target:
        return right
    return partial_search()


logging.basicConfig(
    level=logging.DEBUG,
    filename="b_search.log",
    filemode="w",
    format="[%(levelname)s]\t%(message)s"
)

if __name__ == '__main__':
    print('Ожидается 2', broken_search([0, 1, 2], 2))
    print('Ожидается 2', broken_search([1, 2, 0], 0))
    print('Ожидается 1', broken_search([1, 2, 0], 2))
    print('Пример 1. 6', broken_search([19, 21, 100, 101, 1, 4, 5, 7, 12], 5))
    print('Пример 2. 1', broken_search([5, 1], 1))
