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

class interval_node():
	"""
	as we said we modify the RBT.
	so, every node stores
	"""
	def __init__(self, interval):
		self.intt = interval
		self.max = interval.end
		self.left = None
		self.right = None

def insert(INTNode, interval):
	if INTNode == None:
		return interval_node(interval)

	low = INTNode.intt.begin

	if interval.begin < low:
		INTNode.left = insert(INTNode.left, interval)

	else:
		INTNode.right = insert(INTNode.right, interval)

	if INTNode.max < interval.high:
		INTNode.max = interval.high

	return INTNode

def 






		