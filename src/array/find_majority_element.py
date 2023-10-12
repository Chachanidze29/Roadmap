# [2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2]

def find_majority_element(nums):
    n = int(len(nums) / 2)
    m = {}
    for num in nums:
        if num not in m:
            m[num] = 1
        else:
            m[num] += 1

    for num, c in m.items():
        if c > n:
            print(num)
            return
    print(-1)


def boyer_moore(nums):
    res = -1
    c = 0
    for i in range(len(nums)):
        if c == 0:
            res = nums[i]
            c = 1
        elif res == nums[i]:
            c += 1

    print(res)


if __name__ == '__main__':
    find_majority_element([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2])