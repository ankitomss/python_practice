def find(s, i, curstr):
    if i == len(s):
        return [curstr]

    ret = []
    if s[i] == "?":
        ret += find(s, i+1, curstr+"1")
        ret += find(s, i+1, curstr+"0")
    else:
        ret += find(s, i+1, curstr+s[i])

    return ret

def stringCombinations(s):
    return find(s, 0, "")

print stringCombinations("10??101")