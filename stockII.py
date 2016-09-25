# this is the problem buy one and sell one multiple times; but only one stock should be held with
def stockII(nums):
    n=len(nums)
    max_so_far=nums[n-1]
    profit=0
    for i in range(n-1, -1, -1):
        if nums[i] > max_so_far:
            max_so_far=nums[i]
        else:
            profit+=max_so_far-nums[i] if max_so_far>nums[i] else 0
            max_so_far=nums[i]

    return profit

def stock_II(nums):
    profit=0
    for i in range(1, len(nums)):
        diff=nums[i]-nums[i-1]
        if diff>0:
            profit+=diff
    return profit

