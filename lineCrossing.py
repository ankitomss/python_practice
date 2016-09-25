def isLineCrossing(nums):
    if len(nums) <=3:
        return False

    n=len(nums)
    for i in range(3, n):
        if x[i] >= x[i-2] and x[i-1] <= x[i-3]: return False
        if i>=4:
            if x[i]+x[i-4] >= x[i-2] and x[i-1]==x[i-3]: return False

        if i>=5:
            if x[i-2] - x[i-4] >= 0 and x[i] >= x[i-2] - x[i-4] and x[i-1] >= x[i-3] - x[i-5] and x[i-1] <= x[i-3]:
                return True

    return False


