def is_invalid_num(num):
    if type(num) is not int or num < 0:
        return True
    else:
        return False


def find_duplicate(nums, start_index=0):
    length = len(nums)
    if start_index >= (length - 1) or length == 1:
        return False

    for i in range(start_index + 1, length):
        if is_invalid_num(nums[i]) or is_invalid_num(nums[start_index]):
            return False
        if nums[start_index] == nums[i]:
            return nums[start_index]
    return find_duplicate(nums, start_index + 1)
