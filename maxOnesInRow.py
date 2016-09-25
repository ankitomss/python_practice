def count(nums):

    n=len(nums)
    s,e=0, n
    if nums[n-1]==0: return 0

    while s<=e:
        m=(s+e)/2

        if s==e:
            if nums[s]==0:
                return n-s-1
            else:
                return n-s
        elif nums[m]==0:
            s=m+1
        elif nums[m]==1:
            e=m-1

    if nums[s]==0:
        return n-s-1
    else:
        return n-s

nums=[1]
print count(nums)


mat=[[0 ,1 ,1, 1],
[0 ,0 ,1 ,1],
[1 ,1 ,1 ,1],
[0, 0 ,0 ,0]]
def findMaxOne(mat):
    m,n=len(mat), len(mat[0])
    max=0
    for i in range(m):
        if max < count(mat[i]):
            index=i
            max=count(mat[i])

    return index


print findMaxOne(mat)
