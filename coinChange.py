import sys
def findChange(coins, k):
    dp=[sys.maxint]*(k+1)

    dp[0]=0
    for i in range(k+1):
        for coin in coins:
            if coin <= i: dp[i]=min(dp[i], 1+dp[i-coin])

    return dp[k]


coins=[1,2,5]
k=11

print findChange(coins,k)