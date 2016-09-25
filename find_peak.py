def find_peak(nums):
    s, e = 0, len(nums) - 1
    while s<=e:
        m = (s+e)/2
        if s==e:
            return nums[s]
        elif e == s+1:
            return max(nums[s], nums[e])
        elif nums[m] > nums[m-1] and nums[m] > nums[m+1]:
            return nums[m]
        elif nums[m] < nums[m-1]:
            e = m-1
        elif nums[m] < nums[m+1]:
            s = m+1

nums = [10, 20, 15, 2, 23, 90, 67]
nums1 = [10, 20, 30, 40, 50]
print find_peak(nums1)