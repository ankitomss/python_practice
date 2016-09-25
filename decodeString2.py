def decodeString(s, curset, result):
    if not s:
        result.append(curset)
        return
    if len(s)==1:
        tocheck=s[:1]
        decodeString(s[1:], curset+chr(int(tocheck)+ord('a')-1), result)
        return

    for i in range(1,3):
        tocheck=s[:i]
        if int(tocheck) <= 26:
            decodeString(s[i:], curset+chr(int(tocheck)+ord('a')-1), result)

s='121'
result=[]
decodeString(s, "", result)

print result
