class interval:
	"""interval class which stores
	begin and end of interval and
	also performs get_begin() and
	get_end() operations"""
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
	def get_begin(self):
		return self.begin
	def get_end(self):
		return self.end

class nilNone:
	def __init__(self):
		self.is_red = False

NIL = nilNone()


class interval_node:
	"""
	as we said we modify the RBT.
	so, every node stores
	"""
	def __init__(self, interval):
		self.intt = interval
		self.max_till_now = interval.end
		self.parent = NIL
		self.left = NIL
		self.right = NIL

class interval_tree:
	"""interval tree class"""
	def __init__(self, root = NIL)
	self.root = root

	def insert(self, i_node):
		"""This insert will be similar to RB_insert
		we'll have to modify max_till_now of each ancestor
		of newly inserted node"""

		if self.root == NIL:
			self.root = i_node

		

		





		