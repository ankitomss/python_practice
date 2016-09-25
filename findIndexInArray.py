def findindex(nums, n):
    l=len(nums)
    if nums[0] >= n: return 0
    if nums[l-1] < n: return l


    s,e=0,l-1
    while s<=e:
        m=(s+e)/2

        if nums[m]==n:
            return -1
        elif s==e:
            return s if n < nums[s] else s+1
        elif n < nums[m]:
            e=m-1
        else:
            s=m+1

    return s

nums=[1,3,5,6,7,9,11]
n=10
print findindex(nums,n)