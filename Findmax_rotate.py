def findmax(nums):
    n=len(nums)
    s,e=0,n-1

    if nums[s] < nums[e]:
        return nums[e]
    while s<=e:
        m=(s+e)/2

        if s==e:
            return nums[s] if nums[s] > nums[e] else nums[e]
        elif nums[m] > nums[m+1] and nums[m] > nums[m-1]:
            return nums[m]
        elif nums[m] > nums[s]:
            s=m+1
        else:
            e=m-1
    return nums[s]

nums=[3,1]
print findmax(nums)
