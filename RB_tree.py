

class nilNode:
	def __init__(self):
		self.is_red = False

NIL = nilNode()

class RBNode:
	def __init__(self, key, is_red = True,
					left = NIL, right = NIL,
					parent = NIL):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None
		self.is_red = False

class RBTree:
	def __init__(self, root = NIL):
		self.root = NIL

def left_rotate(T, x):
	y = x.right
	x.right = y.left
	if y.left != NIL:
		y.left.parent = x
	y.parent = x.parent
	if x.parent == NIL:
		T.root = y
	elif x == x.parent.left:
		x.parent.left = y
	else:
		x.parent.right = y
	y.left = x
	x.parent = y

def right_rotate(T, y):
	x = y.left
	y.left = x.right
	if x.right != NIL:
		x.right.parent = y
	x.parent = y.parent
	if y.parent == NIL:
		T.root = x
	elif y = y.parent.left:
		y.parent.left = x
	else:
		y.parent.right = x
	x.right = y
	y.parent = x

def RB_Insert_FIXUP(T, z):

	while z.parent.is_red == True:

		if z.parent = z.parent.parent.left:
			y = z.parent.parent.right 		#Finding z's uncle
			if y.is_red == True:			#z's uncle is red (case-1)
				z.parent.is_red = False
				y.is_red = False
				z.parent.parent.is_red = True
				z = z.parent.parent

			else:
				if z == z.parent.right:		#in case if z is a right child we will left_roate (case-2)
					z = z.parent
					left_rotate(T, z)
				z.parent.is_red = False		#case-3
				z.parent.parent.is_red = True
				right_rotate(T, z.parent.parent)

		else:
			y = z.parent.parent.left
			if y.is_red == True:
				z.parent.is_red = False
				y.is_red = False
				z.parent.parent.is_red = True
				z = z.parent.parent

			else:
				if z == z.parent.left:
					z = z.parent
					right_rotate(T, z)
				z.parent.is_red = False
				z.parent.parent.is_red = True
				left_rotate(T, z.parent.parent)
	T.root.is_red = False


def RB_Insert(T, z):
	y = NIL
	x = T.root
	while x != NIL:
		y = x
		if z.key < x.key:
			x = x.left
		else:
			x = x.right
	z.parent = y

	if y == NIL:
		T.root = z
	elif z.key < y.key:
		y.left = z
	else:
		y.right = z
	z.left = NIL
	z.right = NIL
	z.is_red = True
	RB_Insert_FIXUP(T,z)



def RB_delete(T, z):
	y = z
	

