import sys
def dfs(mat, visited, i, j):
    mx = 0
    m, n = len(mat), len(mat[0])

    for x, y in [(1, 0), (0,1), (-1, 0), (0, -1)]:
        xx, yy = i +x, j+y
        if xx >= 0 and yy >= 0 and xx < m and yy < n and mat[i][j] < mat[xx][yy] and not visited[xx][yy]:
            visited[xx][yy] = 1

            mx = max(dfs(mat, visited, xx, yy), mx)
            visited[xx][yy] = 0
    return 1+mx


def longest_increasing_path(mat):
    m, n = len(mat), len(mat[0])
    visited = [[0 for i in range(n)] for j in range(m)]
    maxsofar = -sys.maxint + 1
    for i in range(m):
        for j in range(n):
            visited[i][j] = 1
            maxsofar = max(dfs(mat, visited, i, j), maxsofar)

            visited[i][j] = 0
    return maxsofar


def cal_dp(i, j, mat, dp):
    m, n = len(mat), len(mat[0])
    if i<0 or j<0 or i >=m or j>=n:
        return 0

    if dp[i][j]:
        return dp[i][j]

    for x, y in [(1,0), (0,1), (-1,0), (0,-1)]:
        xx, yy = x+i, y+j
        if xx >= 0 and yy >= 0 and xx < m and yy < n and mat[xx][yy] < mat[i][j]: dp[i][j] = max(dp[i][j], cal_dp(xx, yy, mat, dp))
    dp[i][j] += 1
    return dp[i][j]

def longest_increase_dp(mat):
    m, n = len(mat), len(mat[0])
    dp = [[0 for i in range(n)] for j in range(m)]
    return max(cal_dp(i, j, mat, dp) for i in range(m) for j in range(n))

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

print longest_increase_dp(nums)