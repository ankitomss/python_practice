def largestNumber(nums):
    slist=[str(nums[i]) for i in range(len(nums))]
    slist.sort(cmp=lambda a,b:cmp(a+b,b+a))
    print slist 
    slist.reverse()
    print slist
    return "".join(slist)


nums=[3, 30, 34, 5, 9]
print largestNumber(nums)