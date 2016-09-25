"""
Minimum number of swaps required for arranging pairs adjacent to each other
There are n-pairs and therefore 2n people. everyone has one unique number ranging from 1 to 2n.
All these 2n persons are arranged in random fashion in an Array of size 2n. We are also given who is partner of whom.
Find the minimum number of swaps required to arrange these pairs such that all pairs become adjacent to each other.

solution: possibilities first two elements could be pairs or not
http://www.geeksforgeeks.org/minimum-number-of-swaps-required-for-arranging-pairs-adjacent-to-each-other/
"""


def minswaps(n, pairs, arr):
    if not n:
        return 0

    x, y = arr[0], arr[1]
    if pairs[x] == y:
        return minswaps(n-1, pairs, arr[2:])
    else:
        return 1 + min(minswaps(n-1, pairs, arr), minswaps(n-1, pairs, arr))


def solve(n, pp, arr):
    if not n:
        return 0

    pairs = {}
    for p in pp:
        pairs[p[0]] = p[1]
        pairs[p[1]] = p[0]
