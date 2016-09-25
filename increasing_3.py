num = [1,2,0,3,2]
def increasing_three(nums):
    dp = [1 for i in range(len(nums))]
    maxlen = 1
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                maxlen = max(dp[i], maxlen)

    return maxlen

print increasing_three(num)