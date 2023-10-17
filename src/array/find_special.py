# Given an integer array, determine the index of an element
# before which all elements are smaller and after which all are greater.

def find_special(nums):
    for i in range(len(nums)):
        left_side = nums[:i + 1]
        right_side = nums[i:]
        if nums[i] == max(left_side) and nums[i] == min(right_side):
            return i

    return -1


def find_special2(nums):
    pass


if __name__ == '__main__':
    print(find_special([4, 2, 3, 5, 1, 6, 9, 7]))