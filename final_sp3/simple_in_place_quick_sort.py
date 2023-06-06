import logging


def q_sort(nums, left, right) -> None:
    logging.info('.' * 60)
    logging.info(f'nums={nums} left={left} right={right}')
    if left == right:
        logging.info(f'left={left} == right={right}')
        return
    if right - left == 1:
        logging.info(f'right={right} - left={left} == 1')
        if nums[left] > nums[right]:
            logging.info(f'nums[left]={nums[left]} > nums[right]={nums[right]}')
            nums[left], nums[right] = nums[right], nums[left]
            logging.info(f'{left} {right} {nums} \'swap\'')
        return
    start = left
    end = right
    pivot = nums[left]
    logging.info(f'"{pivot}" {start} {left} {right} {end} {nums}')
    while left < right:
        while nums[left] < pivot and left < right - 1:
            left += 1
            logging.info(f'left={left} nums[{left}]={nums[left]}')
        while nums[right] >= pivot and right > left + 1:
            right -= 1
            logging.info(f'right={right} nums[{right}]={nums[right]}')
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            logging.info(f'\'{pivot}\' {start} {left} {right} {end} {nums} \'swap\'')
        right -= 1
        if left < right:
            left += 1
    if left > start:
        q_sort(nums, start, left - 1)
        q_sort(nums, left, end)
    q_sort(nums, left + 1, end)


nums = [4, 8, 9, 20, 1, 5, 3, 10]
# nums = [4, 6, 2, 2, 4]
logging.basicConfig(
    level=logging.INFO,
    filename="q_sort.log",
    filemode="w",
    format="[%(levelname)s] %(message)s"
)
q_sort(nums, 0, len(nums) - 1)
print(nums)
