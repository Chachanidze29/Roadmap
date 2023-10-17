# Find the index that divides an array into two non-empty subarrays with equal sum

def non_empty_same_sum_subarray(nums):
    if not nums:
        return -1

    total = sum(nums)
    left_sum = nums[0]

    for i in range(1, len(nums) - 1):
        if left_sum == total - (nums[i] + left_sum):
            return i
        left_sum += nums[i]

    return -1


if __name__ == '__main__':
    print(non_empty_same_sum_subarray([-1, 6, 3, 1, -2, 3, 3]))
