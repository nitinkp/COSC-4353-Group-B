import numpy as np
import pandas

class Graph:
	# Class that represents the node and edge graph. Also contains functions for adding and removing 	nodes and edges, naming and storing graphs.
	def __init__(self, name, adjMatrix):
		self.name = name
		self.adjMatrix = adjMatrix
		self.nodeCount = self.getNodeCount()
		self.edgeCount = self.getEdgeCount()
	# Set name
	# Set's name of graph
	def setName(self,name):
		self.name = name

	# Get name
	# Get's name of graph
	def getName(self):
		return self.name

	# Insert node
	# Inserts node into graph (need to figure out about edge connections)
	def insertNode(self):
		# print(adjMatrix)
		# # Increment the number of nodes we have
		# graph.nodes = nodes + 1
		# # Need to add both row and column of zeros to adjacency matrix
		# # first create row of 0's
		# newRow = np.zeros(nodes)
		# # Append this to the end of the current matrix
		# print(adjMatrix.append(adjMatrix, nodes))
		# # Reset the current array with new values
		# # ADD IN NEW COLUMN OF 0's
		pass

	# Insert edge
	# Inserts edge into graph (needs a source node and destination node, undirected or directed, can be self referencing)
	def insertEdge(self, a, b):
		# Check if the edge values are out of place first
		if((a > self.nodeCount or a < 1) or (b > self.nodeCount or b < 1)):
			print("Node index out of bounds")
			return -1
		
		# Need to make copy of adjMatrix and then resave it
		# print(self.adjMatrix)
		# print(a)
		# print(b)
		newMatrix = self.adjMatrix
		newMatrix[int(a-1),int(b-1)] = 1
		newMatrix[int(b-1),int(a-1)] = 1
		print("Edge added between nodes " + str(a) + " and " + str(b))
		self.adjMatrix = newMatrix
		# print(self.adjMatrix)
			
	# Remove node
	# Removes node from graph (needs to remove related edges from node that was removed)
	def removeNode(value):
		# Remove both row and column from adjacency matrix
		pass
	# Remove edge
	# Removes edge from between two nodes (needs node a, node b, and edge. Need to work on how multiple edges work)
	def removeEdge(a, b):
		# Sets edge value in matrix to 0
		# adjMatrix.itemset((a,b), 0)
		pass
	# Get node
	# Returns a node in the graph (prob really returns its positon in the adjenccy matrix?)
	def getNode():
		pass
	# Get edge
	# Returns edge in graph (Edge by itself isn't that great, maybe a tuple with the two nodes the edge connects (on one node if its self referencing) Direction too?)
	def getEdge():
		pass
	# Set node
	# Sets the value of a given node. Node has to exist. Data could be anything, need to respect pandas
	def setNode():
		pass
	# Set edge
	# Sets the value and direction of an edge between two nodes (or one node if self referencing)
	def setEdge(self, a, b, value):
		pass
	# Find node
	# Trys to find if node exists in graph. This does not count as a search algorithm and could linearly search through the whole list (O(n) nodes to search)
	def findNode():
		pass
	# Find edge
	# Trys to find if edge exists in graph. This also does not count as a search algorithm.
	def findEdge():
		pass
	# NodeCount
	# Gets count of number of nodes in graph
	def getNodeCount(self):
		# Call dim on passed in matrix to get node count
		nodeCount = self.adjMatrix.shape
		return nodeCount[0]
	# EdgeCount
	# Gets count of number of nodes in graph
	def getEdgeCount(self):
		# Use numpy to grab the unique count of 1's and 0's
		unique, count = np.unique(self.adjMatrix, return_counts = True)
		d = dict(zip(unique, count))
		edgeCount = int((d.get(1))/2)
		return edgeCount
		