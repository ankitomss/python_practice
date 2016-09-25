class Solution(object):
    
    def short(self, s, i, j):
        if i == j+1: return True, 0
        if i == j+2: return True, -1
        
        if s[i] == s[j]: 
            flag, l = self.short(s, i+1, j-1)
            if flag == True:
                return True, l+2
            
        flag, l = self.short(s,i,j-1)
        if(flag == True): return True, l
        return false, 0
        
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ""
        i,j=0,len(s)-1
        flag, l=self.short(s, i, j)
        return s[l:][::-1]+s



	
s2=Solution()
#print s2.shortestPalindrome(s)

