"""
F(i, j)  represents the maximum value the user can collect from
         i'th coin to j'th coin.

    F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ),
                   Vj + min(F(i+1, j-1), F(i, j-2) ))
Base Cases
    F(i, j)  = Vi           If j == i
    F(i, j)  = max(Vi, Vj)  If j == i+1
link: http://www.geeksforgeeks.org/dynamic-programming-set-31-optimal-strategy-for-a-game/
"""
def pickMaximum(a):

    n = len(a)
    dp = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        dp[i][i] = a[i]

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            if l == 2:
                dp[i][j] = max(a[i], a[j])
                continue

            dp[i][j] = max(a[i] + min(dp[i+2][j], dp[i+1][j-1]), \
                        a[j] + min(dp[i][j-2], dp[i+1][j-1]))

    return dp[0][n-1]


a = [8, 15, 3, 7]
print pickMaximum(a)