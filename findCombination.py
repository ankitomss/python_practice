# this method finds out all the possible string replacing ? by either 0 or 1

def findcombination(s, k, result):
    n = len(s)
    if k == n:
        result.append(s)
        return

    findcombination(s[:k] + '0' + s[k + 1:], k + 1, result) or findcombination(s[:k] + '1' + s[k + 1:], k + 1, result) \
        if s[k]=='?' \
        else findcombination(s, k + 1, result)




result = []
s = '101101?1?1?0'
findcombination(s, 0, result)
print result
