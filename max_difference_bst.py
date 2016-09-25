import sys
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.max = -sys.maxint + 1


def max_difference_ancestor(nd, maxsofar):
    if not nd: return sys.maxint

    if not nd.left and not nd.right:
        return nd.val

    mn = min(max_difference_ancestor(nd.left, maxsofar), max_difference_ancestor(nd.right, maxsofar))
    nd.max = nd.val - mn
    maxsofar[0] = max(maxsofar[0], nd.max)
    return min(mn, nd.val)

nd = TreeNode(8)
nd.left = TreeNode(3)
nd.right = TreeNode(10)
nd.right.right = TreeNode(14)
nd.right.right.left = TreeNode(13)
nd.left.left = TreeNode(1)
nd.left.right = TreeNode(6)
nd.left.right.left = TreeNode(4)
nd.left.right.right = TreeNode(7)
maxsofar = [-sys.maxint + 1]
max_difference_ancestor(nd, maxsofar)
print maxsofar[0]









