def increaseDecrease(nums):
    s, e=0, len(nums)-1

    while s<=e:
        m=(s+e)/2

        if s==e:
            return nums[s]
        elif nums[m] > nums[m+1] and nums[m] > nums[m-1]:
            return nums[m]
        elif nums[m] < nums[m+1]:
            s=m+1
        elif nums[m] > nums[m+1]:
            e=m-1
    return nums[m]

nums=[2, 3, 4, 5, 6, 7, 8, 6, 4, 3, 2]
nums1=[3,4,3,2,1]
print increaseDecrease(nums1)



