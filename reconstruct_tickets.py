from collections import defaultdict


def dfs(nd, mp, itr, total, visited):
    if len(itr) == total:
        return True
    itr.append(nd[0])
    visited[nd[1]] = 1
    for node in mp[nd[0]]:
        if not visited[node[1]] and dfs(node, mp, itr, total, visited):
            return True
    del itr[-1]
    return False


def reconstruct_tickets(tickets):
    mp = defaultdict(list)
    for i in range(len(tickets)):
        mp[tickets[i][0]].append((tickets[i][1], i))

    for k,v in mp.iteritems():
        mp[k] = sorted(v)

    start = "JFK"

    total = len(tickets)
    itr = ["JFK"]

    for nd in mp[start]:
        visited = [0 for i in range(len(tickets))]
        if dfs(nd, mp, itr, total, visited) == True:
            return itr

    return []

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print reconstruct_tickets(tickets)