class TreeNode(object):
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None

def findSubTree(a, b):

    if (not a and not b):
        return True
    if not a or not b:
        return False

    if a.val==b.val:
        return findSubTree(a.right, b.right) and findSubTree(a.left, b.left)
    else:
        return findSubTree(a.left, b) or findSubTree(a.right, b)


a=TreeNode(1)
a.left=TreeNode(2)
a.right=TreeNode(3)
a.left.left=TreeNode(4)
a.left.right=TreeNode(5)
a.right.right=TreeNode(6)
a.left.left.left=TreeNode(7)

b=TreeNode(2)
b.left=TreeNode(4)
b.right=TreeNode(5)
b.left.left=TreeNode(8)

print findSubTree(a,b)