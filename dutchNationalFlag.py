def dutchFlag(nums):

    n=len(nums)
    low, mid, high=0,0,n-1  #00000low-111111,mid,,,,,,,high22222

    while mid<=high:
        if nums[mid]==0:
            nums[mid], nums[low]=nums[low], nums[mid]
            low+=1
        elif nums[mid]==1:
            mid+=1
        elif nums[mid]==2:
            nums[mid], nums[high]=nums[high], nums[mid]
            high-=1


    return nums


nums=[1,1,1,1,0,0,0,0,2,0,0,2,1,2]
nums=dutchFlag(nums)

n=len(nums)
for i in range(n):
    print nums[i]