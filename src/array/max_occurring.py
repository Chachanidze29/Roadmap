# Given a non-empty integer array, find the index of the maximum occurring element with an equal probability.

import random


def max_occurring(nums):
    m = {}
    for i in range(len(nums)):
        if nums[i] not in m:
            m[nums[i]] = [i]
        else:
            m[nums[i]].append(i)

    max_key = max(m, key=lambda key: len(m[key]))
    return random.choice(m[max_key])


if __name__ == '__main__':
    print(max_occurring([4, 3, 6, 8, 4, 6, 2, 4, 5, 9, 7, 4]))
