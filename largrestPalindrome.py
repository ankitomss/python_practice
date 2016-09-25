def longestPalindrome(A):
        s=A
        n=len(s)
        dp=[[0 for i in range(n)] for j in range(n)]
        
        maxl=1
        mstr=s[0]
        for i in range(n):
            dp[i][i]=1
            
        for i in range(n-1):
            if s[i]==s[i+1]:
                if maxl == 1: mstr=s[i:i+2]
                maxl=2
                dp[i][i+1]=2
                
        
        for k in range(3, n+1):
            for i in range(n-k+1):
                j=i+k-1
                if s[i] == s[j]:
                    if dp[i+1][j-1]!=0:
                        dp[i][j]=2+dp[i+1][j-1]
                    
                    if dp[i][j] > maxl:
                        mstr=s[i:j+1]
                    maxl=max(maxl, dp[i][j])
                    
        
        return mstr

print longestPalindrome("ababab")
