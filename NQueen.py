def isvalid(nums, i, j):

    n=len(nums)

    for jj in range(n):
        if nums[i][jj] or nums[jj][j]: return False

    for ii in range(n):
        if ii==0: continue
        elif i-ii>-1 and j-ii>-1 and nums[i-ii][j-ii]: return False
        elif i+ii<n and j+ii<n and nums[i+ii][j+ii]: return False
        elif i+ii<n and j-ii>-1 and nums[i+ii][j-ii]: return False
        elif i-ii>-1 and j+ii<n and nums[i-ii][j+ii]: return False

    return True


def place(mat, k, n):
    if k==n:
        return mat

    for j in range(n):
        if isvalid(mat, k, j):
            mat[k][j]=1
            placing=place(mat, k+1, n)
            if placing:
                return placing
            mat[k][j]=0

    return None


def solve(n):
    mat=[[0 for k in range(n)] for l in range(n)]

    i=0
    return place(mat, i, n)



print solve(4)




