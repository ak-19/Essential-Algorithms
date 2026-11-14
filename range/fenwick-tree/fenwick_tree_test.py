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

    def test_range_boundaries(self):
        for query in (self.tree.get_range, self.tree.sumRange):
            for left, right in ((0, 0), (7, 7), (0, 7), (0, 3), (3, 7)):
                with self.subTest(query=query.__name__, left=left, right=right):
                    self.assertEqual(query(left, right), sum(self.values[left:right + 1]))

    def test_range_out_of_bounds(self):
        for query in (self.tree.get_range, self.tree.sumRange):
            for left, right in ((-1, 3), (0, -1), (0, 8), (8, 8), (-2, -1)):
                with self.subTest(query=query.__name__, left=left, right=right):
                    with self.assertRaises(IndexError):
                        query(left, right)

    def test_reversed_range(self):
        for query in (self.tree.get_range, self.tree.sumRange):
            with self.subTest(query=query.__name__):
                with self.assertRaises(ValueError):
                    query(4, 1)

    def test_index_out_of_bounds(self):
        for index in (-1, 8):
            for method in (self.tree.get_val, self.tree.get_prefix,
                           self.tree.update, self.tree.construct):
                with self.subTest(method=method.__name__, index=index):
                    args = (index, 99) if method.__name__ in ("update", "construct") else (index,)
                    with self.assertRaises(IndexError):
                        method(*args)
        self.assertEqual(self.tree.get_range(0, 7), sum(self.values))

    def test_boundary_updates(self):
        self.tree.update(0, -10)
        self.tree.update(7, 0)
        self.assertEqual(self.tree.get_range(0, 0), -10)
        self.assertEqual(self.tree.get_range(7, 7), 0)
        self.assertEqual(self.tree.get_range(0, 7), 17)

    def test_single_element(self):
        tree = FenwickTree([5])
        self.assertEqual(tree.get_range(0, 0), 5)
        tree.update(0, -2)
        self.assertEqual(tree.sumRange(0, 0), -2)

    def test_empty_tree(self):
        tree = FenwickTree([])
        for query in (tree.get_range, tree.sumRange):
            with self.subTest(query=query.__name__):
                with self.assertRaises(IndexError):
                    query(0, 0)


if __name__ == "__main__":
    unittest.main()
