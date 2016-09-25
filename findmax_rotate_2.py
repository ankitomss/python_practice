def findmax(nums):
    s, e = 0, len(nums) - 1
    while s <= e:
        m = (s+e)/2

        if s == e:
            return nums[s]
        elif s == e-1:
            return max(nums[s], nums[e])
        elif nums[m] >= nums[m-1] and nums[m] >= nums[m+1]:
            return nums[m]
        elif nums[m] >= nums[s]:
            s = m+1
        else:
            e = m-1


nums = [6, 9, 10,12, 15,1, 3, 5]
print findmax(nums)