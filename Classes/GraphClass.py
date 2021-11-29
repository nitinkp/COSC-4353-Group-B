import numpy as np
import pandas

class Graph:
	# Class that represents the node and edge graph. Also contains functions for adding and removing 	nodes and edges, naming and storing graphs.
	def __init__(graph, nodeCount, edgeCount, name):
		graph.name = name
		# Add in more for graph information
		# Numpy matrix
		# NEED TO FIX THIS AS PROPER MATRIX
		#adjMatrix = np.arrange(6)
		adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
		

		# Nodes list
		nodes = []
		graph.nodeCount = nodeCount
		# Edge list
		edges = []
		graph.edgeCount = edgeCount

	# Set name
	# Set's name of graph
	def setName(name):
		graph.name = name

	# Get name
	# Get's name of graph
	def getName():
		return graph.name

	# Insert node
	# Inserts node into graph (need to figure out about edge connections)
	def insertNode(graph):
		print(adjMatrix)
		# Increment the number of nodes we have
		graph.nodes = nodes + 1
		# Need to add both row and column of zeros to adjacency matrix
		# first create row of 0's
		newRow = np.zeros(nodes)
		# Append this to the end of the current matrix
		print(adjMatrix.append(adjMatrix, nodes))
		# Reset the current array with new values
		# ADD IN NEW COLUMN OF 0's
	# Insert edge
	# Inserts edge into graph (needs a source node and destination node, undirected or directed, can be self referencing)
	def insertEdge(a,b):
		# Sets edge value between two nodes to 1
		adjMatrix.itemset((a,b), 1)
	# Remove node
	# Removes node from graph (needs to remove related edges from node that was removed)
	def removeNode(value):
		# Remove both row and column from adjacency matrix
		pass
	# Remove edge
	# Removes edge from between two nodes (needs node a, node b, and edge. Need to work on how multiple edges work)
	def removeEdge(a, b):
		# Sets edge value in matrix to 0
		adjMatrix.itemset((a,b), 0)
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
	def setEdge():
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
	def getNodeCount(graph):
		return graph.nodeCount
	# EdgeCount
	# Gets count of number of nodes in graph
	def getEdgeCount(self):
		return graph.edgeCount