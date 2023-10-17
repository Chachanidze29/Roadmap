# Find a pair with a minimum absolute sum in an array

import sys


def abs_min_sum(nums):
    if len(nums) < 2:
        return

    low, high = 0, len(nums) - 1
    i = j = 0

    m = sys.maxsize

    while low < high:
        if abs(nums[high] + nums[low]) < m:
            m = abs(nums[high] + nums[low])
            (i, j) = (low, high)

        if m == 0:
            break

        if nums[high] + nums[low] < 0:
            low += 1
        else:
            high -= 1

    return nums[i], nums[j]


if __name__ == '__main__':
    print(abs_min_sum([-6, -5, -3, 0, 2, 4, 9]))
