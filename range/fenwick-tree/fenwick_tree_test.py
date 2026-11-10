import unittest

from fenwick_tree import FenwickTree


class FenwickTreeTest(unittest.TestCase):
    def setUp(self):
        self.values = [1, 2, 3, 4, 5, 6, 7, 8]
        self.tree = FenwickTree(self.values.copy())

    def test_get_val(self):
        self.assertEqual(self.tree.get_val(1), 2)

    def test_get_range(self):
        self.assertEqual(self.tree.get_range(1, 4), 14)

    def test_update(self):
        self.tree.update(1, 11)
        self.assertEqual(self.tree.get_range(1, 4), 23)

    def test_sum_range(self):
        self.tree.update(1, 11)        
        self.assertEqual(self.tree.sumRange(1, 4), 23)


if __name__ == "__main__":
    unittest.main()
