def dfs(node, visited, result):
    if visited[node.val]==True:
        return

    visited[node.val]=True
    result.append(node.val)
    for node in adjacency[node]:
        dfs(node, visited, result)


def find(nodes):

    visited=[False for node in nodes]
    ret=[]
    for node in nodes:
        if not visited[node.val]:
            result=[]
            dfs(node, visited, result)
            ret.append(result)

    return ret

