def area_histogram(nums):
    s = []
    i, n = 0, len(nums)
    maxarea, area = 0, 0
    while i < n:
        print s
        if not s or nums[s[-1]] <= nums[i]:
            s.append(i)
            i += 1
        else:
            tp = s.pop()

            ll = i if not s else i - s[-1] -1

            area = ll * nums[tp]
            print area
            maxarea = max(area, maxarea)

    print s
    while s:
        tp = s.pop()
        ll = i if not s else i - s[-1] -1
        area = ll * nums[tp]
        print area
        maxarea = max(area, maxarea)

    return maxarea

nums = [6, 2, 5, 4, 5, 1, 6]
nums1 = [3, 2, 1]
print area_histogram(nums)

