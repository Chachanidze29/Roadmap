# For an array A consisting n elements, index i is an equilibrium index
# if the sum of elements of subarray A[0…i-1] is equal to the sum of elements of subarray A[i+1…n-1]. i.e.

# [0, -3, 5, -4, -2, 3, 1, 0]

def equilibrium_index(nums):
    for i in range(0, len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            print(i)


if __name__ == '__main__':
    equilibrium_index([0, -3, 5, -4, -2, 3, 1, 0])
