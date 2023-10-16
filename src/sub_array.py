def sub_array(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            print(nums[i:j + 1])


if __name__ == '__main__':
    sub_array([1, 2, 3])
