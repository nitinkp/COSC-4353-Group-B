import unittest
import minimizeFeature as mf


class TestMin(unittest.TestCase):
    def test_nodes(self):
        n = mf.nodes
        self.assertIsInstance(n, int)


if __name__ == '__main__':
    unittest.main()
