def findmax(nums):
    n=len(nums)
    s, e=0, n-1

    while s<=e:
        m=(s+e)/2
        if s==e:
            return s
        elif nums[m]>nums[m-1] and nums[m]>nums[m+1]:
            return m
        elif nums[m]>nums[m-1]:
            s=m+1
        elif nums[m]<nums[m-1]:
            e=m-1
    return s


def binarysearch(nums,x, i, j, order):
    s, e=i, j

    while s<=e:
        m=(s+e)/2
        if nums[m]==x:
            return m
        elif s==e:
            return -1
        elif nums[m]>x:
            if order: e=m-1
            else:s=m+1
        elif nums[m]<x:
            if order:s=m+1
            else: e=m-1
    return -1

def findele(nums, x):
    n=len(nums)
    m=findmax(nums)
    k=binarysearch(nums, x, 0, m, 1)
    l=binarysearch(nums, x, m+1, n-1, 0)

    if l==-1 and k==-1:
        return -1
    elif l==-1:
        return k
    elif k==-1:
        return l

nums=[1,3,5,6,8,4,2,0]
print findele(nums,3)
print findmax(nums)


