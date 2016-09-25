"""
Given a string return the longest palindrome that can be constructed by removing or shuffling characters.

Example:
'aha' -> 'aha'
'ttaatta' -> ' ttaaatt'
'abc' -> 'a' or 'b' or 'c'
'gggaaa' -> 'gaaag' or 'aggga'

"""
def longestPalindrome(s):
    ss, dd = set(), []
    for c in s:
        if ss and c in ss:
            dd.append(c)
            ss.discard(c)
        else:
            ss.add(c)

    return "".join(dd) + (list(ss)[0] if ss else "") + "".join(dd[::-1])

ret = longestPalindrome("abc")
print len(ret), ret