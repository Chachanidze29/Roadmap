def squares_sorted1(arr):
    if len(arr) == 0:
        return arr

    squared_arr = [x ** 2 for x in arr]
    return sorted(squared_arr)


def squares_sorted2(arr):
    res = [0 for _x in arr]
    left = 0
    right = len(arr) - 1
    for i in range(len(arr) - 1, 0, -1):
        left_squared = arr[left] ** 2
        right_squared = arr[right] ** 2
        if left_squared > right_squared:
            res[i] = left_squared
            left += 1
        else:
            res[i] = right_squared
            right -= 1

    return res


if __name__ == '__main__':
    print(squares_sorted2([-10,-7,-5,1,2,3,5,8,100]))
