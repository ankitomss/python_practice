def memDP(nums, i, j, mem):
    if i>j:
        return [""]
    if i==j and int(nums[i])!=0:
        mem[i][j]=[chr(int(nums[i])+96)]
        return mem[i][j]

    if mem[i][j]:
        return mem[i][j]

    if int(nums[i]!=0):
        _next= memDP(nums, i+1, j, mem)
        ls=[chr(int(nums[i])+96) + _next[k] for k in range(len(_next))]

    if int(nums[i]) < 3 or (int(nums[i])==2 and int(nums[i+1])<=7):
        _next= memDP(nums, i+2, j, mem)
        ls+=[chr(int(nums[i:i+2])+96) + _next[k] for k in range(len(_next))]

    mem[i][j]=ls
    return ls


def recursivehelp(nums, curstr, result):
    if not nums:
        result.add(curstr)
        return

    x=int(nums[0])
    if len(nums)>=2: y = int(nums[1])
    if x!=0:
        recursivehelp(nums[1:], curstr+chr(int(nums[0])+96),result)
    if (x>0 and x<3) or (x==2 and y<=7):
        recursivehelp(nums[2:], curstr+chr(int(nums[0:2])+96), result)




def DPhelp(nums):
    no=[int(nums[i]) for i in range(len(nums))]
    if no[0]==0: return
    mp={nums[0]:nums[1:]}
    n=len(nums)
    dp=[[""] for i in range(n+1)]


    for i in range(1,n+1):
        if no[i-1]!=0:
            dp[i]=[dp[i-1][j]+chr(no[i-1]+96) for j in range(len(dp[i-1]))]
        if i==1: continue

        if (no[i-2]>0 and no[i-2] <3) or (no[i-2]==2 and no[i-1] <=7):
            dp[i]+=[dp[i-2][j]+chr(int(nums[i-2:i])+96) for j in range(len(dp[i-2]))]
    #print dp
    return dp[n]

def decodeString(nums):

    curstr=""
    result=set()
    #recursivehelp(nums, curstr, result)
    n=len(nums)
    mem=[[[] for j in range(n)] for i in range(n)]
    print memDP(nums, 0, n-1, mem)

    #print result

nums="121"
decodeString(nums)






