def max_sum_by_digits(nums):
    nums.sort(reverse=True)
    x_num, y_num = 0, 0
    for i in range(0, len(nums), 2):
        x_num *= x_num * 10 + nums[i]
        y_num = y_num * 10 + nums[i+1]
    return x_num + y_num


if __name__ == '__main__':
    print(max_sum_by_digits([4, 6, 2, 7, 9, 8]))
