import sys
def greatestRight(nums):
    n=len(nums)
    _max=[-1]*n
    _max[n-1]=-1
    _maxsofar=-sys.maxint+1
    for i in range(n-2,-1,-1):
        if nums[i+1]>_maxsofar:
            _maxsofar=nums[i+1]
        _max[i]=_maxsofar

    return _max

print greatestRight([6,5,4,2,3,3,2,2,1,1,1])

