# Find the minimum difference between the index of two given elements present in an array

import sys


def find_min_diff(A, x, y):
    if len(A) <= 1:
        return 0

    x_index = y_index = len(A)
    min_diff = sys.maxsize

    for i in range(len(A)):
        if A[i] == x:
            x_index = i
            if y_index != len(A):
                min_diff = min(min_diff, abs(x_index - y_index))
        if A[i] == y:
            y_index = i
            if x_index != len(A):
                min_diff = min(min_diff, abs(x_index - y_index))

    return min_diff


if __name__ == '__main__':
    print(find_min_diff([1, 3, 5, 4, 8, 2, 4, 3, 6, 5], 2, 5))
