class listnode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def printlist(self, nd):
        while nd:
            print nd.val
            nd = nd.next

