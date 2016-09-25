import string

def wordLadder(start, end, wordDict):
    wordDict.add(end)
    q=set([start])
    prev={start:[]}
    added=[]
    while q:


        for word in list(q):
            for c in string.ascii_lowercase:
                for i in range(len(word)):
                    totest=word[:i]+c+word[i+1:]
                    if totest in wordDict:
                        q.add(totest)
                        added.append(totest)
                        prev[totest]=prev.get(totest,[])+[word]
            q.remove(word)

        while added:
            wordDict.discard(added.pop())

        if end in q:
            break

    return prev


def print_ladder(start, end, prev, curls, result):
    if start == end:
        result.append(curls)
        return

    for last in prev[end]:
        print_ladder(start, last, prev, curls+[last], result)





wordDict=set(["hot","dot","dog","lot","log"])
start, end='hit', 'cog'
curls=[end]
result=[]
print_ladder(start, end, wordLadder(start,end, wordDict), curls, result)
print result



