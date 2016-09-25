class TrieNode(object):
    def __init__(self):
        self.word=None
        self.children={}

class Trie(object):
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        root=self.root
        for char in word:
            root=root.children.setdefault(char, TrieNode())
        root.word=word

class solution(object):
    def search(self, i, j, root, m, n, r):
        char=board[i][j]
        if not char and not char in root.children:
            return

        board[i][j], root=None, root.children[char]
        if root.word:
            r.append(root.word)
            root.word
