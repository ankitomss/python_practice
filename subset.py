def choose(nums, k, curset, res):
    if not k:
        res.append(curset)
        return

    if not nums:
        return

    choose(nums[1:], k, curset, res)
    choose(nums[1:], k-1, curset + [nums[0]], res)

def subset(nums):
    res = []
    for i in range(1, len(nums)+1):
        cur = []
        choose(nums, i, cur, res)

    return res

nums = [1,2,3,4,5]
print subset(nums)
