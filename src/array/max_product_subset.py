# -6, 4, -5, 8, -10, 0, 8
import sys


def max_product_subset(nums):
    n = len(nums)

    if n == 0:
        return 0

    if n == 1:
        return nums[1]

    product = 1
    neg_count = 0
    pos_count = 0
    abs_min = sys.maxsize
    contains_zero = False

    for i in range(n):
        if nums[i] < 0:
            neg_count += 1
            abs_min = min(abs_min, abs(nums[i]))

        elif nums[i] > 0:
            pos_count += 1

        if nums[i] == 0:
            contains_zero = True
        else:
            product *= nums[i]

    if neg_count & 1:
        product /= -abs_min
    if neg_count == 1 and pos_count == 0 and contains_zero:
        product = 0
    if neg_count == 0 and pos_count == 0 and contains_zero:
        product = 0

    return product


if __name__ == '__main__':
    print(max_product_subset([-6, 4, -5, 8, -10, 0, 8]))
