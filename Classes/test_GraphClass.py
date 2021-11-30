import unittest
from GraphClass import Graph
import numpy as np

class TestGraph(unittest.TestCase):

    def test_setName(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        test.setName("Graph1")
        self.assertEqual(test.name, "Graph1")

    def test_getName(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        pass
    
    def test_insertNode(self):
        pass

    def test_insertEdge(self):
        pass

    def test_removeNode(self):
        pass

    def test_removeEdge(self):
        pass

    def test_setEdgeWeight(self):
        pass

    def test_getEdgeWeight(self):
        pass

    def test_getNodeCount(self):
        pass

    def test_getEdgeCount(self):
        pass

    def test_getMatrix(self):
        pass

    def test_save(self):
        pass

