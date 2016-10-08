"""
https://www.hackerrank.com/contests/world-codesprint-7/challenges/two-characters/copy-from/7239287
"""

#!/bin/python

import sys
import collections

# s_len = int(raw_input().strip())
# s = raw_input().strip()

s_len =375
s = "uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon"

ss = set()
for c in s:
    ss.add(c)

unique, dp = list(ss), collections.defaultdict(list)
#print unique
for i in range(len(unique)):
    for j in range(i+1, len(unique)):
        key = unique[i]+unique[j]
        dp[key] = [1 for k in range(s_len)]


for i in range(1, len(s)):
    for j in range(i):
        if s[j] != s[i]:
            key = s[j]+s[i]
            if key not in dp:
                key = key[::-1]

            dp[key][i] = max(dp[key][j] + 1, dp[key][i])
            #print key, i, dp[key][i]
            #mmax = max(dp[key][i], mmax)

#print dp
maxx = 0
for k, v in dp.iteritems():
    print k, v[s_len-1]
    maxx = max(v[s_len-1], maxx)

res = ""
for c in s:
    if c == "i" or c =="n":
        res += c

print res, len(res)
print maxx
