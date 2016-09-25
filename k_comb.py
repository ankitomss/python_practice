def kcomb(nums, curcomb, result, k, i):
    if len(curcomb) == k:
        result.append(curcomb)
        return

    if i >= len(nums):
        return

    kcomb(nums, curcomb+str(nums[i]), result, k, i+1)
    kcomb(nums, curcomb, result, k, i+1)


nums = [1, 2, 3, 4, 5]
curcomb = ""
result = []
kcomb(nums, curcomb, result, 3, 0)
print result, len(result)