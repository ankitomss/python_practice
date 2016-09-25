class TreeNode(object):
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

def viewleft(head, curlevel, maxlevel):
    if not head:
        return

    if curlevel>maxlevel[0]:
        print head.val
        maxlevel[0]=curlevel

    viewleft(head.left, curlevel+1, maxlevel)
    viewleft(head.right, curlevel+1, maxlevel)

def leftview(head):
    curlevel,maxlevel=0,[-1]
    viewleft(head, curlevel, maxlevel)


head=TreeNode(1)
head.left=TreeNode(2)
head.right=TreeNode(3)
head.right.left=TreeNode(4)
head.right.right=TreeNode(5)
head.right.right.left=TreeNode(6)
leftview(head)


