class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common(nd, x, y):
    if nd.val == x or nd.val == y:
        return nd.val
    elif nd.val > x and nd.val < y:
        return nd.val
    elif nd.val > x and nd.val > y:
        return lowest_common(nd.left, x, y)
    else:
        return lowest_common(nd.right, x, y)

nd = TreeNode(5)
nd.left = TreeNode(2)
nd.right = TreeNode(8)
nd.right.left = TreeNode(6)
nd.right.right = TreeNode(9)
nd.right.left.right = TreeNode(7)

print lowest_common(nd, 6, 9)