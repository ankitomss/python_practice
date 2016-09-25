class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
    
class Solution(object):
    def dfs(self, root, flag):
        if not root:
            return 0

        if flag:
            return root.val+self.dfs(root.left, 0)+self.dfs(root.right, 0)
        else:
            return max(self.dfs(root.left, 0)+self.dfs(root.right, 0),  \
                        self.dfs(root.left, 0)+self.dfs(root.right, 1), \
                        self.dfs(root.left, 1)+self.dfs(root.right, 1), \
                        self.dfs(root.left, 1)+self.dfs(root.right, 0))

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return max(self.dfs(root, 1) , self.dfs(root, 0))