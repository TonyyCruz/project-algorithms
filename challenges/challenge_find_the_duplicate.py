def is_invalid_num(num):
    if not isinstance(num, int) or num < 0:
        return True
    else:
        return False


def find_duplicate(nums):
    length = len(nums)
    if length <= 1:
        return False
    nums.sort()

    for i in range(1, length):
        if is_invalid_num(nums[i - 1]) or is_invalid_num(nums[i]):
            return False
        if nums[i - 1] == nums[i]:
            return nums[i]
    return False
