"""
Assignment-2, Problem-2

problem statement:
Avoid Roads: https://community.topcoder.com/stat?c=problem_statement&pm=1889
"""

#This class is defined for better understanding
#of code. It just stores x and y coordinate
class node:
	def __init__(self, i, j):
		self.x = i
		self.y = j

#This class is defined to connect two nodes
#and check if the edge in bad between them
class edge:
	def __init__(self, node1, node2, bad):
		self.sn = node1
		self.en = node2
		self.is_bad = self.get_bad(bad)

	def get_bad(self, bad):
		if ("%d %d %d %d" %(self.sn.x, self.sn.y, self.en.x, self.en.y) in bad):
			return True
		else:
			return False

#This function takes arguments
#w = width, h= height and bad = bad edges
"""
Recurrance function
dp[i][j] = { 1 if i,j =0
			0 if i or j = 0 and edge is bad
			dp[i-1,j] or dp[i,j-1] if i or j = 0 and edge is not bad
			dp[i-1,j] if i,j != 0 and one edge is bad
			dp[i,j-1] if i,j != 0 and one edge is bad
			dp[i-1,j] + dp[i, j-1] if i,j != 0 and edges are good 
"""

def numWays(w, h, bad):
	dp = [[None]*(w+1) for i in range(h+1)]

	for i in range(h+1):
		for j in range(w+1):
			if i == 0:
				if j == 0:
					dp[i][j] = 1
				elif edge(node(i,j-1), node(i, j), bad).is_bad:
					dp[i][j] = 0
				else:
					dp[i][j] = dp[i][j-1] 
			elif j == 0:
				if i == 0:		#this condition is already checked but to maintain sync I'm doing this
					dp[i][j] = 1	
				elif edge(node(i-1,j), node(i,j), bad).is_bad:
					dp[i][j] = 0
				else:
					dp[i][j] = dp[i-1][j]
			else:
				if edge(node(i,j-1), node(i,j), bad).is_bad:
					dp[i][j] = dp[i-1][j]
				elif edge(node(i-1,j), node(i,j), bad).is_bad:
					dp[i][j] = dp[i][j-1]
				else:
					dp[i][j] = dp[i-1][j] + dp[i][j-1]

	return dp[h][w]


if __name__ == '__main__':
	width = 35
	height = 31
	bad = {}

	n = numWays(width, height, bad)

	print n
