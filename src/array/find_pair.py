# Given an unsorted integer array, find a pair with the given sum in it.

# nums = [8, 7, 2, 5, 3, 1]
# target = 10

def find_pair(nums, target):
    for x in nums:
        for y in nums:
            if x + y == target:
                print("Pair found (", x, ',', y, ")")
                return
    print("Pair not found")


def find_pair2(nums, target):
    nums = sorted(nums)
    low = 0
    high = len(nums) - 1
    while low < high:
        if nums[low] + nums[high] == target:
            print("Pair found (", nums[low], ',', nums[high], ")")
            return

        if nums[low] + nums[high] < target:
            low += 1
        else:
            high -= 1
    print("Pair not found")


def find_pair3(nums, target):
    m = {}
    for i in range(0, len(nums) - 1):
        if (target - nums[i]) in m:
            print("Pair found (", nums[i], ',', nums[m[target - nums[i]]], ")")
            return
        m[nums[i]] = i
    print("Pair not found")


def find_pair_extended(nums, target):
    m = {}
    printed = {}
    for i in range(0, len(nums) - 1):
        if (target - nums[i]) in m and not nums[i] in printed:
            print("Pair found (", nums[i], ',', nums[m[target - nums[i]]], ")")
            printed[nums[i]] = True
        m[nums[i]] = i
    if printed:
        return
    print("Pair not found")


if __name__ == '__main__':
    find_pair_extended([8, 7, 2, 8, 2, 5, 3, 1], 10)
