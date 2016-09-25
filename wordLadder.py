import string

def word_ladder(start, end, wordDict):
    wordDict.add(end)
    q=set()
    q.add(start)
    level=0
    while q:
        level+=1
        for word in list(q):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    tocheck=word[:i]+c+word[i+1:]
                    if tocheck in wordDict:
                        q.add(tocheck)
            q.discard(word)
            if end in q:
                return level

    return -1


wordDict=set(["hot","dot","dog","lot","log"])
start, end='hit', 'cog'
print word_ladder(start, end, wordDict)