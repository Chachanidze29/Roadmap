def duplicates_in_range(nums, k):
    m = {}
    end = min(k, len(nums) - 1)

    for i in range(0, end):
        if nums[i] in m:
            print(nums[i])
        m[nums[i]] = 1


if __name__ == '__main__':
    duplicates_in_range([5, 6, 8, 2, 4, 6, 9], 10)
