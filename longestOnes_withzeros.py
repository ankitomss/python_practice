def findlongest(nums):
    prev_zero, prevprev_zero, temp, index=-1,-1,-1,-1
    max_so_far=0
    n=len(nums)
    for i in range(n):
        if nums[i]==0:
            prevprev_zero=prev_zero
            prev_zero=temp
            temp=i
            if max_so_far <  temp-prevprev_zero-1:
                max_so_far=temp-prevprev_zero-1
                index=prev_zero


    if max_so_far < n-prevprev_zero-1:
        max_so_far=n-prevprev_zero-1
        prev_zero=temp
        index=prev_zero

    return index

nums=[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
nums1=[0,0,1,1]
print findlongest(nums1)