
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.values = key

def preorder(root):
	if root:
		print root.values
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print root.values

def inorder(root):
	if root:
		inorder(root.left)
		print root.values
		inorder(root.right)

def tree_search(root, x):
	if root==None or root.values == x:
		return root
	if x<root.values:
		return tree_search(root.left, x)
	else:
		return tree_search(root.right, x)

def iterative_tree_search(root, k):
	while x != None and root.values != key:
		if k < root.values:
			root = root.left
		else:
			root = root.right
	return root

def insert_bst(root, new_node):
	if root == None:
		root = new_node
	else:
		if new_node.values < root.values:
			if root.left == None:
				root.left = new_node
			else:
				insert_bst(root.left, new_node)
		else:
			if root.right == None:
				root.right = new_node
			else:
				insert_bst(root.right, new_node)

def find_minimum_value_node(root):
	if root == None:
		return root
	while(root.left != None):
		root = root.left
	return root

def delete_bst(root, x):
	if root == None:
		return root

	if x < root.values:
		root.left = delete_bst(root.left, x)
	elif x > root.values:
		root.right = delete_bst(root.right, x)

	else:
		if root.right == None:
			temp = root.left
			root= None
			return temp
		elif root.left == None:
			temp = root.right
			root = None
			return temp

		temp = find_minimum_value_node(root.right)
		root.values = temp.values
		root.right = delete_bst(root.right, temp.values)

	return root

root = Node(50)

insert_bst(root, Node(30))
insert_bst(root, Node(20))
insert_bst(root, Node(40))
insert_bst(root, Node(70))
insert_bst(root, Node(60))
insert_bst(root, Node(80))

inorder(root)

delete_bst(root, 20)

inorder(root)

delete_bst(root, 50)

inorder(root)




