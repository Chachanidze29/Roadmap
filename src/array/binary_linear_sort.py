# { 1, 0, 1, 0, 1, 0, 0, 1 }

def binary_linear_sort(nums):
    zero_count = 0
    for x in nums:
        if x == 0:
            zero_count += 1
    result = [0] * len(nums)
    for i in range(1, len(nums)):
        if i >= zero_count:
            result[i] = 1

    return result


if __name__ == '__main__':
    print(binary_linear_sort([1, 0, 0, 0, 0, 0, 0, 1]))
