import matplotlib.pyplot as plt
from collections import defaultdict
import time

class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	def addEdge(self, start_node, end_node, weight):
		self.graph.append([start_node,end_node,weight])

	def printArr(self, dist):
		print("Vertex Distance from Source")
		for i in range(self.V):
			print("%d \t\t %d"%(i, dist[i]))

	def BellmanFord(self, source):
		dist = [float("Inf")]*self.V
		dist[source] = 0

		for i in range(self.V - 1):

			for u,v,w in self.graph:
				if dist[u] != float("Inf") and dist[u] + w < dist[v]:
					dist[v] = dist[u] + w

		for u,v,w in self.graph:
			if dist[u] != float("Inf") and dist[u] + w < dist[v]:
				print "Grpah has negative weight cycle"
				return
		self.printArr(dist)

if __name__ == '__main__':
	
	g = Graph(5)
	g.addEdge(0,1,6)
	g.addEdge(0,2,7)
	g.addEdge(4,0,2)
	g.addEdge(1,3,5)
	g.addEdge(3,1,-2)
	g.addEdge(1,2,8)
	g.addEdge(1,4,-4)
	g.addEdge(2,3,-3)
	g.addEdge(2,4,8)
	g.addEdge(4,3,7)

	t1 = time.clock()

	g.BellmanFord(0)
	print time.clock() - t1
	