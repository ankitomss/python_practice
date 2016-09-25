def increasing_triplet(nums):
    n=len(nums)
    if not n or n<2:
        return False

    m1, m2=n-1, -1
    for i in range(n-2, -1, -1):
        if m2 is not -1 and nums[i] < nums[m1] and nums[i] < nums[m2]:
            return True
        elif nums[i] < nums[m1] and (m2 is -1 or nums[i] > nums[m2]):
            m2=i
        elif nums[i] > nums[m1]:
            m1=i
            m2=-1

    return False

nums=[1,2,3,4,5]
nums1=[5,4,3,2,1]
print increasing_triplet(nums1)


