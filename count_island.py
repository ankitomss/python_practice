mat = [[1, 1, 0, 0, 1, 1],
       [1, 1, 0, 0, 1, 1],
       [0, 0, 0, 0, 1, 1],
       [1, 0, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 1],]


def count_island(mat):
    m, n = len(mat), len(mat[0])
    visited = [[0 for i in range(n)] for j in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and mat[i][j]:
                count += 1
                dfs(mat, visited, i, j)
    return count


def dfs(mat, visited, x, y):
    visited[x][y] = 1
    m, n = len(mat), len(mat[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            xx, yy = x+i, y+j
            if xx > -1 and yy > -1 and xx < m and yy < n and mat[xx][yy] and not visited[xx][yy]:
                dfs(mat, visited, xx, yy)

print count_island(mat)