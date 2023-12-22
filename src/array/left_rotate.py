# Left rotate array k times

def left_rotate_k(nums, k=1):
    for _ in range(k):
        left_rotate(nums)

    return nums


def left_rotate(nums):
    first = nums[0]
    for i in range(len(nums) - 1):
        nums[i] = nums[i + 1]

    nums[-1] = first


if __name__ == '__main__':
    print(left_rotate_k([3, 4, 5, 1, 2], 3))
