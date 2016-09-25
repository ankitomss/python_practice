class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):


    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        lchild=self.lowestCommonAncestor(root.left, p, q)
        rchild=self.lowestCommonAncestor(root.right, p, q)

        if root==p or root==q:
            return root
        elif not lchild and not rchild:
            return None
        elif lchild and rchild:
            return root

        return lchild or rchild





