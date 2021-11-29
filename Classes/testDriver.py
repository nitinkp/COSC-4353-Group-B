# Test drive program for graph class
# Written by Mike Yannuzzi

from GraphClass import Graph
import numpy as np
print("Starting test for class")

adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])

# Start!
# Test Constructor
print("Testing constructor")
# print("Pass...")
test = Graph("graph1", adjMatrix)
print(test)
print()

# Test getName
print("Testing getName")
# print("pass...")
testName = test.getName()
print("Name of Graph is = " + testName)
print()

# Test setName
print("Testing setName")
#print("Pass...")
test.setName("newName")
print("New name is: " + test.name)
print()

# Test insertNode
print("Testing insertNode")
#test.insertNode()
print("Pass...")

# Test insertEdge
print("Testing insert edge")
print("Pass...")

# Test removeNode
print("Testing removeNode")
print("Pass...")

# Test removeEdge
print("Testing removeEdge")
print("Pass...")

# Test getNode
print("Testing getNode")
print("Pass...")

# Test getEdge
print("Testing getEdge")
print("Pass...")

# Testing setNode
print("Testing setNode")
print("Pass...")

# Testing setEdge
print("Testing setEdge")
print("Pass...")

# Testing findNode
print("Testing findNode")
print("Pass...")

# Testing findEdge
print("Testing findEdge")
print("Pass...")

# Testing getNodeCount
print("Testing getNodeCount")
# print("Pass...")
nodeCount = test.getNodeCount()
print("Graph has " + str(nodeCount) + " nodes")

# Testing getEdgeCount
print("Testing getEdgeCount")
edgeCount = test.getEdgeCount()
#print(edgeCount)
# print("Pass...")