class Solution(object):
    def match(self, s, p, i, j):
        while i==len(s) and j<len(p) and (p[j]=='*' or p[(j+1) if j<len(p)-1 else j]=='*'): j+=1
        print i, j

        if i>=len(s) and j>=len(p):return True
        if i>=len(s) or j>=len(p): return False

        if j<len(p)-1 and p[j+1] == '*' and (p[j] == '.' or s[i] == p[j]): return self.match(s, p, i, j + 2) or self.match(s,p,i + 1, j)
        if j<len(p)-1 and p[j+1] == '*': return self.match(s,p,i, j + 2)
        if p[j] == '.' or s[i] == p[j]: return self.match(s,p,i + 1, j + 1)
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i,j=0,0
        return self.match(s,p,i,j)


solve=Solution()
s="aaaaaaaaaaaaab"
p="a*a*a*a*a*a*a*a*a*a*c"
print solve.isMatch(s,p)