class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_to_bst(nums):
    if not nums:
        return None
    root = TreeNode(nums[0])
    left = [l for l in nums if l < nums[0]]
    right = [r for r in nums if r > nums[0]]

    root.left = preorder_to_bst(left)
    root.right = preorder_to_bst(right)
    return root


def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print root.val
    in_order_print(root.right)


nums = [4, 2, 3, 8, 7, 9]
root = preorder_to_bst(nums)
in_order_print(root)