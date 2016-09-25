"""
code chef hard problem:
https://www.codechef.com/viewsolution/11629272
Input

The first line of the input contains an integer T denoting the number of trees. The description of T trees follows.

Each test case consists of a single line containing four space separated integers a, b, m and N.

Output

For each test case, output a single line containing a single integer,
 denoting the depth of the node that was inserted last in the binary search tree.
"""

import sys
def calculate(a, b, m, N):
    ldepth, rdepth, mmin, mmax, i, depth = 0, 0, sys.maxint - 1, 0, 1, 0
    while i <= N:
        node = (a + b*i) % m
        if node < mmin:
            ldepth += 1
            mmin = node
        if node > mmax:
            rdepth += 1
            mmax = node
        depth = max(ldepth, rdepth)
        i += 1
    return depth - 1
m = int(raw_input())

while m:
    a, b, mm, N = map(int, raw_input().split())
    print int(calculate(a, b, mm, N))
    m -= 1
