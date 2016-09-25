import collections
def remove_duplicate(s):
    counter = collections.Counter(s)
    st = list()
    resultset = set()
    for c in s:
        counter[c] -= 1
        if c in resultset:
            continue
        while st and st[-1] > c and counter[st[-1]]:
            resultset.remove(st.pop())
        resultset.add(c)
        st.append(c)

    return "".join(st)

print remove_duplicate("adabcd")