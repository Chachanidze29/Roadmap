# Left rotate array k times

def left_rotate(nums, k=1):
    for _ in range(k):
        first = nums[0]
        for i in range(len(nums) - 1):
            nums[i] = nums[i + 1]

        nums[-1] = first

    return nums


if __name__ == '__main__':
    print(left_rotate([3, 4, 5, 1, 2], 3))
