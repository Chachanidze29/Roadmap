def merge_arrays(nums1, nums2):
    if not nums1 and not nums2:
        return []

    if not nums1:
        nums1 = len(nums2) * [0]
    if not nums2:
        nums2 = len(nums1) * [0]

    len1 = len(nums1)
    len2 = len(nums2)

    if len1 < len2:
        nums1 += [0] * (len2 - len1)
    elif len2 < len1:
        nums2 += [0] * (len1 - len2)

    res = []

    for i in range(len(nums2)):
        s = nums1[i] + nums2[i]
        if 10 <= s <= 99:
            res.append(int(str(s)[0]))
            res.append(int(str(s)[1]))
        else:
            res.append(s)

    return res


if __name__ == '__main__':
    print(merge_arrays([23, 5, 2, 7, 87], [4, 67, 2, 8]))
