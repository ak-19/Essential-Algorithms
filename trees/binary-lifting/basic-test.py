import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("basic.py")
SPEC = importlib.util.spec_from_file_location("basic", MODULE_PATH)
basic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(basic)
BinaryLifting = basic.BinaryLifting


class TestBinaryLifting(unittest.TestCase):
    def setUp(self):
        # Tree rooted at 0:
        #
        #          0
        #        /   \
        #       1     2
        #      / \   / \
        #     3   4 5   6
        #        /
        #       7
        self.edges = [
            [0, 1],
            [0, 2],
            [1, 3],
            [1, 4],
            [2, 5],
            [2, 6],
            [4, 7],
        ]
        self.tree = BinaryLifting(8, self.edges)

    def test_depths_are_built_from_root(self):
        self.assertEqual(self.tree.depth, [0, 1, 1, 2, 2, 2, 2, 3])

    def test_kth_ancestor_returns_expected_nodes(self):
        self.assertEqual(self.tree.kth_ancestor(7, 0), 7)
        self.assertEqual(self.tree.kth_ancestor(7, 1), 4)
        self.assertEqual(self.tree.kth_ancestor(7, 2), 1)
        self.assertEqual(self.tree.kth_ancestor(7, 3), 0)
        self.assertEqual(self.tree.kth_ancestor(7, 4), -1)

    def test_kth_ancestor_handles_root(self):
        self.assertEqual(self.tree.kth_ancestor(0, 0), 0)
        self.assertEqual(self.tree.kth_ancestor(0, 1), -1)

    def test_lca_for_same_branch(self):
        self.assertEqual(self.tree.lca(3, 7), 1)
        self.assertEqual(self.tree.lca(4, 7), 4)

    def test_lca_for_different_branches(self):
        self.assertEqual(self.tree.lca(3, 6), 0)
        self.assertEqual(self.tree.lca(5, 6), 2)

    def test_lca_when_nodes_are_equal(self):
        self.assertEqual(self.tree.lca(5, 5), 5)

    def test_distance_between_nodes(self):
        self.assertEqual(self.tree.distance(3, 7), 3)
        self.assertEqual(self.tree.distance(5, 6), 2)
        self.assertEqual(self.tree.distance(7, 6), 5)
        self.assertEqual(self.tree.distance(0, 7), 3)

    def test_nonzero_root_changes_depths_and_ancestors(self):
        tree = BinaryLifting(8, self.edges, root=4)

        self.assertEqual(tree.depth[4], 0)
        self.assertEqual(tree.depth[1], 1)
        self.assertEqual(tree.depth[0], 2)
        self.assertEqual(tree.depth[6], 4)
        self.assertEqual(tree.kth_ancestor(6, 1), 2)
        self.assertEqual(tree.kth_ancestor(6, 4), 4)
        self.assertEqual(tree.lca(3, 7), 4)
        self.assertEqual(tree.distance(3, 6), 4)

    def test_single_node_tree(self):
        tree = BinaryLifting(1, [])

        self.assertEqual(tree.depth, [0])
        self.assertEqual(tree.kth_ancestor(0, 0), 0)
        self.assertEqual(tree.kth_ancestor(0, 1), -1)
        self.assertEqual(tree.lca(0, 0), 0)
        self.assertEqual(tree.distance(0, 0), 0)

    def test_kth_ancestor_rejects_negative_k(self):
        with self.assertRaises(ValueError):
            self.tree.kth_ancestor(7, -1)

    def test_public_queries_reject_invalid_nodes(self):
        with self.assertRaises(IndexError):
            self.tree.kth_ancestor(8, 1)

        with self.assertRaises(IndexError):
            self.tree.lca(-1, 3)

        with self.assertRaises(IndexError):
            self.tree.distance(3, 8)


if __name__ == "__main__":
    unittest.main()
