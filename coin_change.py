def coin_change(coins, num):
    dp = [0 for i in range(num+1)]
    for i in range(1, num+1):
        for coin in coins:
            if coin <= i:
                if not dp[i]:
                    dp[i] = dp[i-coin] + 1
                else:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[num]

coins = [1, 2, 5]
num = 11
print coin_change(coins, num)