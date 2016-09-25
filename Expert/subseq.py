def make(s, curstr, memory):
    if not s:
        if curstr: return [curstr]
        return []

    if s in memory:
        return memory[s]
    ret =[]
    ret = make(s[1:], curstr+s[i], memory) + \
            make(s[1:], curstr, memory)

    memory[s] = ret
    return ret

def  buildSubsequences( s):
    memory = {}
    ret = make(s, "", memory)
    return sorted(ret)


buildSubsequences("abc")