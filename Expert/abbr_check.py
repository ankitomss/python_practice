class Solution(object):
    def isValid(self, word, abbr):
        
        i, j, m, n = 0, 0, len(word), len(abbr)
        while j < len(abbr):
            if i >= m: return False
            elif abbr[j].isdigit():
                tmp = ""
                if abbr[j] == "0": return False
                while j < len(abbr) and abbr[j].isdigit(): 
                    tmp += abbr[j]
                    j += 1
                i += int(tmp)
            elif abbr[j] == word[i]:
                i, j = i+1, j+1
            else:
                return False
                
        return i == m and j == n
        
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        n = len(target)
        for i in range(n, 0, -1):
            for j in range(n-i+1):
                abbr = target[:j] + str(i) + target[j+i:]
                fail = False
                for word in dictionary:
                    if self.isValid(word, abbr):
                        fail = True
                        break
                if not fail: return abbr
            
                
        