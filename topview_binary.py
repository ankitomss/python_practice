class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bfs(nd):
    st = set()
    q = list()
    q.append((nd, 0))
    while q:
        nde = q[0]
        del q[0]
        node, d = nde[0], nde[1]
        if d not in st:
            print node.val
            st.add(d)

        if node.left:
            q.append((node.left, d - 1))

        if node.right:
            q.append((node.right, d + 1))


def top_view(nd):
    bfs(nd)

nd = TreeNode(3)
nd.left = TreeNode(4)
nd.right = TreeNode(5)
nd.right.right = TreeNode(7)
nd.right.right.right = TreeNode(8)
nd.right.left = TreeNode(6)
nd.left = TreeNode(4)
nd.left.left = TreeNode(10)

top_view(nd)
