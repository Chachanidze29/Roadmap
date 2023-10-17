# Find the minimum index of a repeating element in an array

# 5, 6, 3, 4, 3, 6, 6, 4

MAX_VAL = 9999


def repeating_index(nums):
    m = {}
    res = MAX_VAL
    for i in range(len(nums)):
        if nums[i] in m:
            res = min(res, m[nums[i]])
        else:
            m[nums[i]] = i

    return res


if __name__ == '__main__':
    res = repeating_index([5, 6, 3, 4, 3, 6, 6, 4])
    if res == MAX_VAL:
        print('Invalid Input')
    else:
        print(res)
