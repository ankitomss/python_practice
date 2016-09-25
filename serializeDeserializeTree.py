class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None

class codec(object):
    def serialize(self, root):
        if not root:
            return '*'

        return str(root.val)+"|"+self.serialize(root.left)+"|"+self.serialize(root.right)

    def maketree(self, ls, i):
        if ls[i[0]]=="*":
            i[0]+=1
            return None
        root=TreeNode(int(ls[i[0]]))
        i[0]+=1
        root.left=self.maketree(ls,i)
        root.right=self.maketree(ls,i)
        return root

    def ptree(self, root):
        if not root:
            return

        print root.val
        self.ptree(root.left)
        self.ptree(root.right)



    def deserialize(self, s):
        ls=s.split('|')
        i=[0]
        return self.maketree(ls,i)



sol=codec()
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.left=TreeNode(4)
root.right.right=TreeNode(5)

s=sol.serialize(root)
print s
newroot=sol.deserialize(s)
sol.ptree(newroot)
