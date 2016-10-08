# Enter your code here. Read input from STDIN. Print output to STDOUT

import collections
n, m = map(int, raw_input().split())
p = map(int, raw_input().split())
edge = collections.defaultdict(list)
total = sum(p)

for i in range(m):
    u, v = map(int, raw_input().split())
    edge[u-1].append(v-1)
    edge[v-1].append(u-1)

def dfs(u, edge, visited, p, black, white, flag):
    visited[u] = 1
    if flag: white[0] += p[u]
    else: black[0] += p[u]
    #print black, white
    for v in edge[u]:
        if not visited[v]:
            dfs(v, edge, visited, p, black, white, not flag)

def calculate(u, edge, p, n, visited):
    q, nodes, ind = [u], set(list[i for i in range(n)]), set()
    while nodes:
        nodes.discard(u)
        ind.add(u)
        for v in edge[u]:
            nodes.discard(v)


visited, maxx = [0 for i in range(n)], 0
for u in range(n):
    if not visited[u]:
        black, white = [0], [0]
        dfs(u, edge, visited, p, black, white, 0)
        maxx += max(black[0], white[0])
print maxx