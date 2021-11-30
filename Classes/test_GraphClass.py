import unittest
from GraphClass import Graph
import numpy as np

class TestGraph(unittest.TestCase):

    def test_getName(self):
        matrix = np.array(1,1)
        test = Graph("TestGraph",)