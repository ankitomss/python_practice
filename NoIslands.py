def dfs(grid, visited, i, j):
    m, n=len(visited), len(visited[0])
    if i <0 or j <0 or i>=m or j>=n:return
    if visited[i][j] or grid[i][j]=='0': return

    visited[i][j]=1

    for x,y in ((0,-1),(-1,0),(1,0),(0,1)):
        ii,jj=i+x, j+y
        dfs(grid, visited, ii, jj)

def bfs(grid, visited, i, j):
    m,n=len(visited), len(visited[0])
    q=[(i,j)]
    visited[i][j]=1
    while q:
        xy=q[0]
        for _i,_j in ((-1, 0), (0,-1), (1,0), (0,1)):
            ii, jj = xy[0]+_i, xy[1]+_j
            print ii,jj
            if ii <0 or jj<0 or ii>=m or jj>=n: continue
            print grid[ii][jj], ii,jj
            if grid[ii][jj] =='1' and visited[ii][jj]==0:
                print "I shoudl be here"
                visited[ii][jj]=1
                q.append((ii,jj))
        del q[0]


def findIsland(grid):
    if not grid: return 0
    m,n=len(grid), len(grid[0])

    visited=[[0]*n for i in range(m)]
    count=0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and grid[i][j]=='1':
                bfs(grid, visited, i, j)
                print visited
                print "this is the count", count
                count+=1

    return count

grid=[['1','1','1','1','0'],
['1','1','0','1','0'],
['1','1','0','0','0'],
['0','0','0','0','0']]
grid1=[['1','1','0','0','0'],
['1','1','0','0','0'],
['0','0','1','0','0'],
['0','0','0','1','1']]
print findIsland(grid1)