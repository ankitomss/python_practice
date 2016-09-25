"""
There given a 2 Lists with int values. We need to find the longest chain. Eg: L1 = { 2,7,4,8,9,10}, L2 = {1,2,8,9,4}.
Here the solution is 2 (chain is 2,4 or 8,9). Because 7 is present in L1 which is not L2.
"""
def longest_chain(l1, l2):
    n, m = len(l1), len(l2)
    dp = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n):
        for j in range(m):
            if l1[i] == l2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

    for row in dp:
        print row

    return dp[n][m]

l1 = [2,7,4,8, 9,10]
l2 = [1,2,8,9,4]

print longest_chain(l1, l2)