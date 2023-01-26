from challenges.utils.quick_sort import quick_sort


def is_invalid_num(num):
    if type(num) is not int or num < 0:
        return True
    else:
        return False


def find_duplicate(nums):
    length = len(nums)
    if length <= 1:
        return False
    quick_sort(nums)

    for i in range(1, length):
        if is_invalid_num(nums[i - 1]) or is_invalid_num(nums[i]):
            return False
        if nums[i - 1] == nums[i]:
            return nums[i]
    return False
