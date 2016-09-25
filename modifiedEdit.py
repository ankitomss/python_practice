def modifiedEdit(str1, str2):
    m, n= len(str1), len(str2)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=i if j==0 else j
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                #dp[i][j]=1+min(dp[i-1][j], dp[i][j-1])

    print dp
    return dp[m][n]

str1="ankit"
str2="anitk"
print modifiedEdit(str1,str2)
