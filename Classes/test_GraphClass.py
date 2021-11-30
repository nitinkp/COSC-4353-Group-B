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
        name = test.getName()
        self.assertEqual(name, "TestGraph1")
    
    def test_insertNode(self):
        # Check both number of nodes and the matrices are equal
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])

        newMatrix = np.array([[0,1,1,0,0,0],
							[1,0,1,1,1,0],
							[1,1,0,1,0,0],
							[0,1,1,0,1,0],
							[0,1,0,1,0,0]
                            [0,0,0,0,0,0]])

        test = Graph("TestGraph", adjMatrix, False, False)
        self.assertEquals(int(test.nodeCount), 6)
        self.assertTrue(np.array_equal(test.adjMatrix,newMatrix))

    def test_insertEdge(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        test.insertEdge(1,1)
        self.assertEqual(test.adjMatrix(0,0), 1)

    def test_removeNode(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])

        newMatrix = np.array([[0,1,1,1],
							[1,0,1,0],
							[1,1,0,1],
							[1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        test.removeNode(1)
        self.assertTrue(np.array_equal(test.adjMatrix,newMatrix))

    def test_removeEdge(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        pass

    def test_setEdgeWeight(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        pass

    def test_getEdgeWeight(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        pass

    def test_getNodeCount(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        pass

    def test_getEdgeCount(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        pass

    def test_getMatrix(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        pass

    def test_save(self):
        adjMatrix = np.array([[0,1,1,0,0],
							[1,0,1,1,1],
							[1,1,0,1,0],
							[0,1,1,0,1],
							[0,1,0,1,0]])
        test = Graph("TestGraph", adjMatrix, False, False)
        pass

