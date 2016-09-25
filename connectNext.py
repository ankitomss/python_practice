class TreeLinkNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
        self.next=None

class Solution(object):
    def connect(self, root):
        prekid, kid=TreeLinkNode(0)

        while root:
            while root:
                kid.next=root.left
                kid=kid.next or kid
                kid.next=root.right
                kid=kid.next or kid
                root=root.next
            root, kid=prekid.next, prekid


prekid= kid=TreeLinkNode(0)

kid.next=TreeLinkNode(123)
kid=TreeLinkNode(420)
kid=prekid
kid.next=TreeLinkNode(111)
print prekid.val, kid.val, prekid.next.val, kid.next.val



