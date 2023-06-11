import logging
from typing import List


def partition(nums: List[int], left: int, right: int) -> int:
    pivot = nums[left + (right - left) // 2]
    logging.error(f'pivot {left + (right - left) // 2, pivot}')
    while True:
        while nums[left] < pivot:
            left += 1
        while nums[right] > pivot:
            right -= 1
        if left >= right:
            return right
        nums[left], nums[right] = nums[right], nums[left]
        logging.error(f'{left, right} {nums}, \'swap\'')
        left += 1
        right -= 1


def quicksort(nums: List[int], left: int, right: int) -> None:
    logging.debug('.' * 79)
    logging.info(f'nums={nums} left={left} right={right} {nums[left:right + 1]}')
    if left >= 0 and right >= 0 and left < right:
        p = partition(nums, left, right)
        logging.info(f'nums={nums} left={left} right={right} p={p}')
        quicksort(nums, left, p)
        quicksort(nums, p + 1, right)


logging.basicConfig(
    level=logging.DEBUG,
    filename="q_sort.log",
    filemode="w",
    format="[%(levelname)s]\t%(message)s"
)
nums = [4, 8, 9, 20, 1, 5, 3, 10]
logging.critical('*' * 79)
logging.warning(f'{nums}')
quicksort(nums, 0, len(nums) - 1)
print(nums)
nums = [4, 6, 2, 2, 4]
logging.critical('*' * 79)
logging.warning(f'{nums}')
quicksort(nums, 0, len(nums) - 1)
print(nums)
nums = [10, 9, 8, 7, 0]
logging.critical('*' * 79)
logging.warning(f'{nums}')
quicksort(nums, 0, len(nums) - 1)
print(nums)
