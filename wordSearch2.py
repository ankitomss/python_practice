def dfs(board, words, i, j, visited, curword, m, n, result):


    if curword in words:
        result.add(curword)
        return
    if i <0 or j<0 or i>=m or j>=n:
        return

    if visited[i][j]: return
    visited[i][j]=1

    for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
        ii, jj = i + x, j + y
        dfs(board, words, ii, jj, visited, curword+board[i][j], m, n, result)
    visited[i][j]=0


def wordSearch(board, words):

    m,n=len(board), len(board[0])
    visited=[[0]*n for i in range(m)]
    curword, result="", set()
    for i in range(m):
        for j in range(n):
            dfs(board, words, i, j, visited, curword, m, n, result)

    return result

words = ["oath","pea","eat","rain"]
board=[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
visited=[[0]*4]*4
print visited

print wordSearch(board, words)

