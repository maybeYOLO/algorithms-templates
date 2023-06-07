import logging


def q_sort(nums, left, right) -> None:
    logging.debug('.' * 79)
    logging.info(f'nums={nums} left={left} right={right} {nums[left:right + 1]}')
    if left == right:
        logging.info(f'left={left} == right={right}')
        return
    if right - left == 1:
        logging.info(f'right={right} - left={left} == 1')
        if nums[right] < nums[left]:
            logging.info(f'nums[left]={nums[left]} > nums[right]={nums[right]}')
            nums[left], nums[right] = nums[right], nums[left]
            logging.error(f'{left, right} {nums} \'swap\'')
        return
    start = left
    end = right
    pivot = nums[left]
    logging.info(f'"{pivot}" {start} {left, right} {end} {nums}')
    while left < right:
        while nums[left] < pivot and left < right:
            left += 1
            logging.info(f'left={left} nums[{left}]={nums[left]}')
        while  not nums[right] < pivot and right > left:
            right -= 1
            logging.info(f'right={right} nums[{right}]={nums[right]}')
        if left != right:
            nums[left], nums[right] = nums[right], nums[left]
            logging.error(f'\'{pivot}\' {start} {left, right} {end} {nums} \'swap\'')
    logging.debug(f'\'{pivot}\' {start} {left, right} {end} {nums}')
    if left > start:
        logging.warning(f'{start, left - 1} {nums} {nums[start:left]}')
        logging.warning(f'{left, end} {nums} {nums[left:end + 1]}')
        q_sort(nums, start, left - 1)
        q_sort(nums, left, end)
    else:
        logging.warning(f'{left + 1, end} {nums} {nums[left + 1:end + 1]}')
        q_sort(nums, left + 1, end)


nums = [4, 8, 9, 20, 1, 5, 3, 10]
# nums = [4, 6, 2, 2, 4]
# nums = [10, 9, 8, 7, 0]
logging.basicConfig(
    level=logging.DEBUG,
    filename="q_sort.log",
    filemode="w",
    format="[%(levelname)s]\t%(message)s"
)
q_sort(nums, 0, len(nums) - 1)
print(nums)
