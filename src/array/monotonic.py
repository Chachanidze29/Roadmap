# Check if function is monotonic

def check_increasing(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


def check_decreasing(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False

    return True


def check_same(arr):
    for i in range(0, len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return False

    return True


def is_monotonic(arr):
    if len(arr) <= 1:
        return True

    if arr[0] < arr[-1]:
        check = 'increasing'
    elif arr[0] == arr[-1]:
        check = 'same'
    else:
        check = 'decreasing'

    match check:
        case 'increasing':
            return check_increasing(arr)
        case 'decreasing':
            return check_decreasing(arr)
        case 'same':
            return check_same(arr)


if __name__ == '__main__':
    print(is_monotonic([1, 1, 20, 1, 10]))
