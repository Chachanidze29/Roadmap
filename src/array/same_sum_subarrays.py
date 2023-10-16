def same_sum_subarrays(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i:]):
            print(f'The two subarrays are {nums[:i]} and {nums[i:]} having equal sum of {sum(nums[:i])}')
            return

    return -1


def same_sum_subarrays2(nums):
    total_sum = sum(nums)
    sum_so_far = 0

    for i in range(len(nums)):
        if sum_so_far == total_sum - sum_so_far:
            return i
        sum_so_far += nums[i]

    return -1


if __name__ == '__main__':
    nums = [6, -4, -3, 2, 3]
    i = same_sum_subarrays2(nums)
    if i != -1:
        print(nums[:i], nums[i:])