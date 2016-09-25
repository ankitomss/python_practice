
def lexographical(nums):
    if not nums:
            return
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1

    point = i
    nums = nums[:i] + nums[i:][::-1]
    if i > 0:
        k = i
        pivot = nums[i - 1]
        while k < len(nums) - 1 and nums[k] <= pivot:
            k += 1
        if nums[k] != pivot:
            nums = nums[:point - 1] + nums[k] + nums[point:k] + pivot + nums[k+1:]
            # nums[k], nums[i - 1] = nums[i - 1], nums[k]

    return nums

nums = [1,2,3,4,7,6,5]
nums = "ankitverma"
print lexographical(nums)


