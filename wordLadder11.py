import collections, string
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        def dfs(mp, word, endWord, curlist, ret, step, depth):
            if depth > step: return
            if word == endWord:
                ret.append(curlist[::-1])
                return

            for neigh in mp[word]:
                dfs(mp, neigh, endWord, curlist + [neigh], ret, step, depth + 1)



        wordlist.add(beginWord)
        wordlist.add(endWord)
        q = [beginWord] + ["#"]

        mp = collections.defaultdict(list)
        step, shortest = 1, 0
        while q:
            start = q[0]
            del q[0]
            if start is "#":
                if not q: break
                step += 1
                q.append('#')
                continue

            for i in range(len(start)):
                for rc in string.ascii_lowercase:
                    if start[i] == rc: continue
                    newword = start[:i] + rc + start[i+1:]
                    if newword in wordlist:
                        if newword not in q: q.append(newword)
                        mp[newword].append(start)


            if endWord in mp and shortest is 0: shortest = step + 1
            wordlist.discard(start)

        print step, shortest
        ret = []
        print mp
        dfs(mp, endWord, beginWord, [endWord], ret, shortest, 1)
        return ret

obj = Solution()
start = "hit"
end = "cog"
dct = set(["hot","cog","dot","dog","hit","lot","log"])
print obj.findLadders(start, end, dct)