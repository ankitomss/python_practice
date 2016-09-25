class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None

def serialize(head):
    if not head:
        return "_"


    return str(head.val)+"|"+serialize(head.left)+"|"+serialize(head.right)

def _help(ls,i):

    if ls[i[0]]=="_":
        i[0]+=1
        return None

    node=TreeNode(int(ls[i[0]]))
    i[0]+=1
    node.left=_help(ls, i)
    node.right=_help(ls, i)
    return node

def deserialize(s):
    ls=s.split("|")
    i=[0]
    return _help(ls,i)

def _print(head):

    if not head:
        return

    print head.val
    _print(head.left)
    _print(head.right)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.left=TreeNode(4)
root.right.right=TreeNode(5)

_print(deserialize(serialize(root)))

