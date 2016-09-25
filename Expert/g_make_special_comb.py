def make(n, curstr, bb, cc, result):

    if len(curstr) == n:
        result.append(curstr)
        return

    for c in "abc":

        if bb and c == "b": continue
        if cc and c == 'c': continue

        make(n, curstr+c, 1 if c == 'b' else bb, (curstr and curstr[-1] == 'c' and c == 'c'), result)


def make_comb(n):
    if not n: return

    result = []
    make(n, "", 0, 0, result)
    return result

ret = make_comb(6)
print len(ret), ret