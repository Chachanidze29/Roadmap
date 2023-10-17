# Move all zeros present in an array to the end

# [6, 0, 8, 2, 3, 0, 4, 0, 1]

def zeros_to_the_end(nums):
    i = 0
    for num in nums:
        if num:
            nums[i] = num
            i += 1

    for j in range(i, len(nums)):
        nums[j] = 0
    print(nums)


if __name__ == '__main__':
    zeros_to_the_end([6, 0, 8, 2, 3, 0, 4, 0, 1])
