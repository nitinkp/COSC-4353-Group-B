<<<<<<< Updated upstream
class graph:
	#Class that represents the node and edge graph. Also contains functions for adding and removing 	nodes and edges, naming and storing graphs.
=======
#Imports
import numpy
import pandas

class graph:
	# Class that represents the node and edge graph. Also contains functions for adding and removing nodes and edges, naming and storing graphs.
	def __init__(self, node, edge, name):
		self.name = name
		# Add in more for graph information
		# Adjacency matrix

		# Adjacency list

		# node list

		# edge list

		# edge count

		# node count

	# Insert node
	# Inserts node into graph (need to figure out about edge connections)
	
	# Insert edge
	# Inserts edge into graph (needs a source node and destination node, undirected or directed, can be self referencing)

	# Remove node
	# Removes node from graph (needs to remove related edges from node that was removed)

	# Remove edge
	# Removes edge from between two nodes (needs node a, node b, and edge. Need to work on how multiple edges work)

	# Get node
	# Returns a node in the graph (prob really returns its positon in the adjenccy matrix?)

	# Get edge
	# Returns edge in graph (Edge by itself isn't that great, maybe a tuple with the two nodes the edge connects (on one node if its self referencing) Direction too?)

	# Set node
	# Sets the value of a given node. Node has to exist. Data could be anything, need to respect pandas

	# Set edge
	# Sets the value and direction of an edge between two nodes (or one node if self referencing)

	# Find node
	# Trys to find if node exists in graph. This does not count as a search algorithm and could linearly search through the whole list (O(n) nodes to search)

	# Find edge
	# Trys to find if edge exists in graph. This also does not count as a search algorithm.

	# NodeCount
	# Gets count of number of nodes in graph

	# EdgeCount
	# Gets count of number of nodes in graph
>>>>>>> Stashed changes
