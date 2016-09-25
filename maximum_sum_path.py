def findmax_sum_path(nums1, nums2):
    m, n = len(nums1), len(nums2)
    i, j =0, 0
    sum1, sum2, result = 0, 0, 0
    while i < m and j < n:
        if nums1[i] > nums2[j]:
            sum1 += nums1[i]
            i += 1
        elif nums1[i] < nums2[j]:
            sum2 += nums2[j]
            j += 1
        else:
            result += max(sum1, sum2)
            sum1, sum2 = 0, 0
            while i < m and j < n and nums1[i] == nums2[j]:
                result += nums1[i]
                i += 1
                j += 1

    while i < m:
        sum1 += nums1[i]
        i += 1

    while j < n:
        sum2 += nums2[j]
        j += 1

    result += max(sum1, sum2)

nums1 = [2, 3, 7, 10, 12]
nums2 = [1, 5, 7, 8]

print findmax_sum_path(nums1, nums2)






