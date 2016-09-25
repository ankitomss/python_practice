class Solution(object):
    maxword = ""
    def findClosest(self, s, dic):
        q=set()
        q.add(s)
        while q:
            for word in list(q):
                for i in range(len(word)):
                    tocheck=word[:i]+word[i+1:]
                    if tocheck in dic:
                        return tocheck
                    if tocheck: q.add(tocheck)
                q.discard(word)

        return "None exist"

    def findClosestDfs(self, s, dic, cache):
        if s in cache:
            return cache[s]
        if not s:
            return

        for i in range(len(s)):
            tocheck=s[:i]+s[i+1:]
            if tocheck in dic:
                cache[s]=tocheck
                return tocheck

        res=""
        for i in range(len(s)):
            tocheck=s[:i]+s[i+1:]
            ans=self.findClosestDfs(tocheck, dic, cache)
            if ans and len(ans)>len(res):
                res=ans
        cache[s]=res
        return res



s="ankiertvma"
s1="ankvmr"
dic=['ankit','verma', 'ankitv']
print Solution().findClosest(s, dic)
maxword=""
d = Solution()
cache={}
print d.findClosestDfs(s,dic, cache)
