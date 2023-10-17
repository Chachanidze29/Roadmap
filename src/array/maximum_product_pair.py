# Given an integer array, find the maximum product of two integers in it.

# [-10, -3, 5, 6, -2]

def maximum_product_pair(nums):
    if len(nums) <= 2:
        return

    res = {}
    m = 0
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums) - 1):
            if nums[i] * nums[j] > m:
                m = nums[i] * nums[j]
                res[nums[i]] = nums[j]
    if res:
        print(res)
    else:
        print(-1, -1)


def maximum_product_pair2(nums):
    if len(nums) <= 2:
        return

    nums = sorted(nums)
    min_i, min_j = nums[0], nums[1]
    max_i, max_j = nums[-1], nums[-2]

    if min_i * min_j >= max_i * max_j:
        print(min_i, min_j)
        return
    print(max_i, max_j)


def maximum_product_pair3(nums):
    if len(nums) <= 2:
        return

    max_1, max_2 = nums[0], -9999
    min_1, min_2 = nums[0], 9999

    for num in nums[1:]:
        if num > max_1:
            max_2 = max_1
            max_1 = num
        elif num > max_2:
            max_2 = num

        if num < min_1:
            min_2 = min_1
            min_1 = num
        elif num < min_2:
            min_2 = num

    if max_1 * max_2 > min_1 * min_2:
        print(max_1, max_2)
    else:
        print(min_1, min_2)


if __name__ == '__main__':
    maximum_product_pair3([-10, -3, 5, 6, -2])
