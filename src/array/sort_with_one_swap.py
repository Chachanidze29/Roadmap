# Sort an array in one swap whose two elements are swapped

# [3, 8, 6, 7, 5, 9]

def sort_with_one_swap(nums):
    x, y = -1, -1
    prev = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < prev:
            if x == -1:
                x = i - 1
                y = i
            else:
                y = i

        prev = nums[i]

    nums[x], nums[y] = nums[y], nums[x]

    return nums


if __name__ == '__main__':
    print(sort_with_one_swap([3, 8, 6, 7, 5, 9]))