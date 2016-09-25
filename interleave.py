def make(s1, s2, l1, l2, i, j, curstr, ret):
    if i == l1 and j == l2:
        ret.append(curstr)
        return

    if i < l1 and j < l2:
        make(s1, s2, l1, l2, i+1, j, curstr + s1[i], ret)
        make(s1, s2, l1, l2, i, j+1, curstr + s2[j], ret)
    elif i < l1:
        make(s1, s2, l1, l2, i+1, j, curstr + s1[i], ret)
    elif j < l2:
        make(s1, s2, l1, l2, i, j+1, curstr + s2[j], ret)


def interleave(s1, s2):
    ret = []
    l1, l2, i, j = len(s1), len(s2), 0, 0
    make(s1, s2, l1, l2, i, j, "", ret)
    return ret

print interleave("abc", "de")



