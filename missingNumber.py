def missingNum(nums):
    missing=1
    for i in range(len(nums)):
        if nums[i]==missing:
            missing+=1
        elif nums[i]>missing:
            return missing
        elif nums[i]<missing:
            continue

def missing(nums):
    n=len(nums)

    sum=n*(1+n)/2
    for i in range(n):
        sum-=nums[i]
    return sum

nums=[1,2,3,5,6,7]
print missingNum(nums)