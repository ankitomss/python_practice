def findindex(sort, x):
    s, e = 0, len(sort)-1
    if x < sort[s]: return s
    if x > sort[e]: return e+1
    while s<=e:
        m = (s+e)/2

        if s==e:
            return s if x <= sort[s] else s+1
        elif sort[m] == x:
            while sort[m] == x:
                m -= 1
            return m+1
        elif sort[m] < x:
            s = m+1
        elif sort[m] > x:
            e = m-1
    return s


def count_smaller(nums):
    n = len(nums)
    sort = [nums[n-1]]

    ans = [0] * n
    for i in range(n-2, -1, -1):

        index = findindex(sort, nums[i])
        print sort, index
        sort.insert(index, nums[i])

        ans[i] = index
    return ans

nums = [5, 2, 6,2,2, 3]
print count_smaller(nums)