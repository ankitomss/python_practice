def move_zeros(nums):
    first, last = 0, 0
    n = len(nums)
    while first < n and last < n:
        while first < n and nums[first]:
            first += 1
        if first < n-1:
            last = first + 1
        else:
            break
        while last < n and not nums[last]:
            last += 1
        if last < n and first < n:
            nums[first], nums[last] = nums[last], nums[first]
    return nums

nums = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
print move_zeros(nums)
