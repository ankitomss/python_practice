
def lexi_sort(s):
    for i in range(len(s)):
        s[i] = sorted(s[i])

    return s

s = ["ankit", "verma"]

print lexi_sort(s)