import logging

def q_sort(nums, left, right, count) -> None:
    logging.info('.' * 60)
    logging.info(f'nums={nums} left={left} right={right} count={count}')
    if left == right:
        logging.info(f'left={left} == right={right}')
        return
    if right - left == 1:
        logging.info(f'right={right} - left={left} == 1')
        if nums[left] > nums[right]:
            logging.info(f'nums[left]={nums[left]} > nums[right]={nums[right]}')
            nums[left], nums[right] = nums[right], nums[left]
        return
    if count > 10:
        logging.critical('\'count limit\'')
        return
    count += 1
    start = left
    end = right
    pivot = nums[left]
    logging.info(f'"{pivot}" {start} {left} {right} {end} {nums}')
    while left < right - 1:
        while nums[left] < pivot and left < right - 1:
            left += 1
            logging.info(f'left={left} nums[{left}]={nums[left]}')
        while nums[right] >= pivot and right > left+ 1:
            right -= 1
            logging.info(f'right={right} nums[{right}]={nums[right]}')
        if left < right:
            if nums[left] > nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                logging.info(f'\'{pivot}\' {start} {left} {right} {end} {nums} s')
            if left < right - 1:
                left += 1
            if left < right - 1:
                right -= 1
        logging.info(f'`{pivot}` {start} {left} {right} {end} {nums} {count}')
    q_sort(nums, start, left, count)
    q_sort(nums, right, end, count)
    

nums = [4, 8, 9, 20, 1, 5, 3, 10]
logging.basicConfig(
    level=logging.INFO,
    filename="q_sort.log",
    filemode="w",
    format="%(message)s"
)
q_sort(nums, 0, len(nums) - 1, 0)
print(nums)
