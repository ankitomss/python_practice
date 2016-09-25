'''
You are given a graph with no cycles, each node representing different cities and there are stadiums for baseball games in all cities.
Each node contains a value representing the population of the city, and a list of neighbors. (feel free to extend data structure)
Every time there is a baseball game at a city, everyone from all the different cities will go to the city with the baseball game.
Return the maximum traffic between a city and its neighbours when there is a game at that city, for all cities. (Does not have to be sorted)
The total run-time after returning everything should be O(n).

Examples:

Input:
1   2
 \ /
  5
 / \
4   3
Output:
1 14
2 13
3 12
4 11
5 4

'''

def traffic(node, visited, adj, total, result):
    if not node:
        return 0

    ret = node.val
    visited[node] = 1
    maxtraffic = 0
    for neigh in adj[node]:
        if not visited[neigh]:
            x = traffic(neigh, visited, adj, total, result)
            ret += x
            maxtraffic = max(maxtraffic, total - x)

    result[node] = maxtraffic
    return ret

