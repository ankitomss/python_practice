def DFS(result, i, s, rml, rmr, op, curs):
    if i==len(s) and not rml and not rmr and not op:
        result.add(curs)
        return
    if i>len(s):
        return

    if rml <0 or rmr<0 or op<0:
        return

    c=s[i]
    if c=='(':
        DFS(result, i+1, s, rml, rmr, op+1, curs+c)
        DFS(result, i+1, s, rml-1, rmr, op, curs)
    elif c==')':
        DFS(result, i+1, s, rml, rmr, op-1, curs+c)
        DFS(result, i+1, s, rml, rmr-1, op, curs)
    else:
        DFS(result, i+1, s, rml, rmr, op, curs+c)

def remove_invalid(s):
    rml, rmr=0,0
    n=len(s)
    for i in range(n):
        if s[i]=="(": rml+=1
        if s[i]==')':
            if rml!=0: rml-=1
            else: rmr+=1
    curs=""
    result=set()
    DFS(result, 0, s, rml, rmr, 0, curs)
    return list(result)


s='()())()'
print remove_invalid(s)