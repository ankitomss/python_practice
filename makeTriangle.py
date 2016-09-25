def make_triangle(p):
    if not p:
        return []
    result=[]
    for a in range(1, p-1):
        for b in range(a, p-1):
            c=p-(a+b)
            if c<b: continue
            if a+b > c and b+c > a and c+a > b:
                result.append([a,b,c])
                if a==b or b==c: continue
                if b!=c: result.append([a,c,b])
                if a!=b: result.append([b,a,c])
                if c!=a: result.append([c,b,a])

    return result

print make_triangle(7)