class TrieNode(object):
    def __init__(self, s=None):
        self.child = [None for _ in range(26)]
        self.val = s

class Trie(object):

    def __init__(self):
        self.head = TrieNode()

    def add(self, s):
        tmp = self.head
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if tmp.child[idx]:
                tmp = tmp.child[idx]
            else:
                tmp.child[idx] = TrieNode(s[:i+1])
                tmp = tmp.child[idx]

    def search(self, s):
        tmp = self.head
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if tmp.child[idx]:
                tmp = tmp.child[idx]
                if tmp.val == s: return True
            else:
                return False


t = Trie()
t.add("ankit")
t.add("ankitv")
print t.search("ankitm")



