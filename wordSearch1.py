def find(s, dict):
    if not s:
        return True

    #return  reduce(lambda x,y:x or y, [True if s[:i+1] in dict and find(s[i+1:], dict) else False for i in range(len(s))])
    for i in range(len(s)):
        if s[:i+1] in dict:
            if find(s[i+1:], dict)==True:
                return True

    return False


def wordSearch(s, dict):
    if not s or not dict:
        return

    #return find(s, dict)
    n=len(s)
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        for word in dict:
            wlen=len(word)
            if i < wlen: continue
            curword=s[i-wlen:i]
            print curword
            if  curword in dict and dp[i-wlen]:
                dp[i]=dp[i-wlen]
                break
    print dp
    return dp[n]


s="bccdbacdbdacddabbaaaadababadad"
dict=["cbc","bcda","adb","ddca","bad","bbb","dad","dac","ba","aa","bd","abab","bb","dbda","cb","caccc","d","dd","aadb","cc","b","bcc","bcd","cd","cbca","bbd","ddd","dabb","ab","acd","a","bbcc","cdcbd","cada","dbca","ac","abacd","cba","cdb","dbac","aada","cdcda","cdc","dbc","dbcb","bdb","ddbdd","cadaa","ddbc","babb"]
#s="leetcode"
#dict=["leet", "code"]
print wordSearch(s, dict)