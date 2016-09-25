class BST():
	def __init__ (self, rootid):
		self.left=None
		self.right=None
		self.value=rootid
	
	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def setNodeValue(self,val):
		self.value=val
	def getNodeValue(self):
		return self.value

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BST(newNode)
		else:
			tree=BST(newNode)
			tree.right=self.right
			self.right=tree


	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BST(newNode)
		else:
			tree = BST(newNode)
			self.left=tree
			tree.left=self.left

def printTree(tree):
        if tree != None:
        	printTree(tree.getLeftChild())
            	print(tree.getNodeValue())
            	printTree(tree.getRightChild())

def testTree():
    myTree = BST("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)


testTree()


