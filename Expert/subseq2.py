# Complete the function below.
def make(s, memory):
    if not s:
        return [""]

    if s in memory:
        return memory[s]

    result = []
    ret = make(s[1:], memory)
    for val in ret:
        result.append(s[0] + val)
        result.append(val)

    memory[s] = result
    return result

def  buildSubsequences( s):
    memory = {}
    ret = make(s, memory)
    ret.remove("")
    return sorted(ret)

print buildSubsequences("a")

print bin(1)
print hex(int(bin(-1), 2))