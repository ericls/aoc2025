def get_num(nums, rem_length):
    if rem_length == 1:
        return max(nums)
    max_i = None
    max_n = 0
    for idx, n in enumerate(nums):
        if idx + rem_length > len(nums):
            break
        if n > max_n:
            max_i = idx
            max_n = n
            if n == 9:
                break
    return max_n * 10 ** (rem_length - 1) + get_num(nums[max_i + 1 :], rem_length - 1)


def get_value_for_line(line, rem_length):
    return get_num(list(map(int, line)), rem_length)
