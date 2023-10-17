# Given an unsorted integer array, print all pairs with a given difference k in it.

# [1, 5, 2, 2, 2, 5, 5, 4]

def find_pairs_with_difference(nums, k):
    s = set()
    res = {}
    for num in nums:
        if num - k in s:
            res[num] = num - k
        if num + k in s:
            res[num + k] = num

        s.add(num)
    print(res)


if __name__ == '__main__':
    find_pairs_with_difference([1, 5, 2, 2, 2, 5, 5, 4], 3)
