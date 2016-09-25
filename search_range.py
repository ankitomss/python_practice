def search_range(nums, target):
    s,e=0, len(nums)
    match=-1
    while s<=e:
        m=(s+e)/2
        if nums[m]==target:
            match=m
            break
        elif s==e:
            match=s
            break   
        elif nums[m] < target:
            s=m+1
        else:
            e=m-1

    if match==-1: match=s

    if nums[match]!=target:
        return [-1 -1]

    if nums[match]!=target:
        return [-1, -1]

    start=end=match
    while start-1>=0 and nums[start-1]==target:
        start-=1
    while end+1 < len(nums) and nums[end+1]==target:
        end+=1

    return [start, end]

nums=[5, 7, 7, 8, 8, 10]
target=8
print search_range(nums, target)