def max_sum_by_digits(nums):
    if len(nums) <= 1:
        return

    nums.sort(reverse=True)

    x, y = 0, 0
    for i in range(0, len(nums), 2):
        x = x * 10 + nums[i]
        y = y * 10 + nums[i + 1]

    print(f"The two numbers with maximum sum are {x} and {y}")


if __name__ == '__main__':
    input = [4, 6, 2, 7, 9, 8]
    max_sum_by_digits(input)
