import logging

NAME_INDEX = 0
SCORE_INDEX = 1
PENALTY_INDEX = 2


def nums_gt(left_value, right_value) -> bool:
    return left_value[SCORE_INDEX] > right_value[SCORE_INDEX] or (
        left_value[SCORE_INDEX] == right_value[SCORE_INDEX]
        and (left_value[PENALTY_INDEX] < right_value[PENALTY_INDEX] or (
            left_value[PENALTY_INDEX] == right_value[PENALTY_INDEX]
            and left_value[NAME_INDEX] < right_value[NAME_INDEX]
        ))
    )


def nums_ge(left_value, right_value) -> bool:
    return left_value[SCORE_INDEX] > right_value[SCORE_INDEX] or (
        left_value[SCORE_INDEX] == right_value[SCORE_INDEX]
        and (left_value[PENALTY_INDEX] < right_value[PENALTY_INDEX] or (
            left_value[PENALTY_INDEX] == right_value[PENALTY_INDEX]
            and left_value[NAME_INDEX] <= right_value[NAME_INDEX]
        ))
    )


def q_sort(nums, left, right) -> None:
    logging.info('.' * 60)
    logging.info(f'nums={nums} left={left} right={right}')
    if left == right:
        logging.info(f'left={left} == right={right}')
        return
    if right - left == 1:
        logging.info(f'right={right} - left={left} == 1')
        if nums_gt(nums[left], nums[right]):
            logging.info(f'nums[left]={nums[left]} > nums[right]={nums[right]}')
            nums[left], nums[right] = nums[right], nums[left]
            logging.info(f'{left} {right} {nums} \'swap\'')
        return
    start = left
    end = right
    pivot = nums[left]
    logging.info(f'"{pivot}" {start} {left} {right} {end} {nums}')
    while left < right - 1:
        while nums_gt(pivot, nums[left]) and left < right - 1:
            left += 1
            logging.info(f'left={left} nums[{left}]={nums[left]}')
        while nums_ge(nums[right], pivot) and right > left + 1:
            right -= 1
            logging.info(f'right={right} nums[{right}]={nums[right]}')
        if nums_gt(nums[left], nums[right]):
            nums[left], nums[right] = nums[right], nums[left]
            logging.info(f'"{pivot}" {start} {left} {right} {end} {nums} \'swap\'')
        right -= 1
        if left < right:
            left += 1
    if left > start:
        q_sort(nums, start, left - 1)
        q_sort(nums, left, end)
    q_sort(nums, left + 1, end)


nums = [
    ['a', 4, 0],
    ['a', 8, 0],
    ['a', 9, 0],
    ['a', 20, 0],
    ['a', 1, 0],
    ['a', 5, 0],
    ['a', 3, 0],
    ['a', 10, 0],
]
logging.basicConfig(
    level=logging.INFO,
    filename="q_sort.log",
    filemode="w",
    format="[%(levelname)s] %(message)s"
)
q_sort(nums, 0, len(nums) - 1)
print(nums)
