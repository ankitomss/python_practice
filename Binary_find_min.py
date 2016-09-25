class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findmin(self, root, l, r):
        if not root:
            return None

        ret=self.findmin(root.left, l, r)
        if root.val >= l and root.val <=r:
            if not ret: ret=root
        if not ret:
            ret=self.findmin(root.right, l, r)
        return ret

        # if root.val >= l:
        #     lchild=self.findmin(root.left, l, r)
        #     if lchild: return lchild
        #     elif root.val <=r: return root
        #     else: return None
        # elif root.val < l:
        #     rchild=self.findmin(root.right, l, r)
        #     return rchild


root=TreeNode(6)
root.left=TreeNode(2)
root.left.right=TreeNode(4)
root.left.left=TreeNode(1)
root.right=TreeNode(9)
root.right.left=TreeNode(7)
root.right.left.right=TreeNode(8)

print Solution().findmin(root, 3, 6).val





