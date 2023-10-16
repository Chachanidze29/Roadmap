# [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def kedane(nums):
    maximum = max(nums)

    if maximum < 0:
        return maximum

    max_so_far = 0
    max_ending_here = 0

    for num in nums:
        max_ending_here += num
        max_ending_here = max(max_ending_here, 0)
        max_so_far = max(max_so_far, max_ending_here)
        print(num, max_ending_here, max_so_far)

    return max_so_far


if __name__ == '__main__':
    kedane([-2, 1, -3, 4, -1, 2, 1, -5, 4])
