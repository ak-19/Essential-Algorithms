from collections import deque
from typing import List

class BinaryLifting:
    """
    Answer ancestor, lowest-common-ancestor, and tree-distance queries quickly.

    Binary lifting preprocesses a rooted tree so each node stores ancestors at
    powers of two: parent, grandparent, 4-th ancestor, 8-th ancestor, and so on.
    Any upward move can then be decomposed into the binary representation of the
    distance to move.

    The input tree is represented by:
        n: The number of nodes. Nodes are expected to be labeled 0 through n - 1.
        edges: Undirected edges of the tree, where each edge is [u, v].
        root: The node used as the tree root. The root is treated as its own
            ancestor during preprocessing.

    Public attributes:
        n: Number of nodes in the tree.
        root: Root node used for all ancestor relationships.
        LOG: Number of binary lifting levels stored per node.
        depth: depth[v] is the number of edges from root to v.
        up: up[v][j] is the 2^j-th ancestor of v.

    Preprocessing complexity:
        Time: O(n log n)
        Space: O(n log n)

    Query complexity:
        kth_ancestor: O(log n)
        lca: O(log n)
        distance: O(log n)

    Notes:
        This implementation assumes the input edges form a connected tree.
        It does not validate that the graph is connected, acyclic, or has exactly
        n - 1 edges.
    """

    def __init__(
        self,
        n: int,
        edges: List[List[int]],
        root: int = 0,
    ) -> None:
        """
        Build the binary lifting table for a rooted tree.

        Args:
            n: Number of nodes in the tree. Valid node labels are 0 to n - 1.
            edges: Undirected tree edges, with each edge written as [u, v].
            root: Node to use as the root for depths and ancestors.

        Raises:
            IndexError: If root or an edge endpoint is outside the list bounds
                while building the adjacency list or traversal state.
        """
        self.n = n
        self.root = root
        self.LOG = max(1, n.bit_length())

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.depth = [0] * n

        # up[v][j] = 2^j-th ancestor of v
        self.up = [[root] * self.LOG for _ in range(n)]

        self._build(graph)

    def _build(self, graph: List[List[int]]) -> None:
        """
        Populate node depths and all binary ancestors.

        The first breadth-first traversal records each node's depth and immediate
        parent. After that, dynamic programming fills higher ancestors:

            up[node][j] = up[up[node][j - 1]][j - 1]

        In words, the 2^j-th ancestor is found by taking two jumps of length
        2^(j - 1).

        Args:
            graph: Adjacency list for the undirected tree.
        """
        visited = [False] * self.n
        visited[self.root] = True

        queue = deque([self.root])

        # The root is defined as its own parent.
        self.up[self.root][0] = self.root

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if visited[neighbor]:
                    continue

                visited[neighbor] = True
                self.depth[neighbor] = self.depth[node] + 1
                self.up[neighbor][0] = node
                queue.append(neighbor)

        # Build ancestors of lengths 2, 4, 8, ...
        for j in range(1, self.LOG):
            for node in range(self.n):
                halfway = self.up[node][j - 1]
                self.up[node][j] = self.up[halfway][j - 1]

    def kth_ancestor(self, node: int, k: int) -> int:
        """
        Return the k-th ancestor of a node.

        The 0-th ancestor is the node itself, the 1st ancestor is its parent,
        the 2nd ancestor is its grandparent, and so on.

        Args:
            node: Node whose ancestor should be found.
            k: Number of edges to move upward from node.

        Returns:
            The k-th ancestor if it exists, otherwise -1 when the requested
            ancestor is above the root.

        Raises:
            ValueError: If k is negative.
            IndexError: If node is outside the valid range [0, n).

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        if k < 0:
            raise ValueError("k must be non-negative")

        if not 0 <= node < self.n:
            raise IndexError("node is outside the tree")

        if k > self.depth[node]:
            return -1

        bit = 0

        while k:
            if k & 1:
                node = self.up[node][bit]

            k >>= 1
            bit += 1

        return node

    def lca(self, u: int, v: int) -> int:
        """
        Return the lowest common ancestor of two nodes.

        The lowest common ancestor is the deepest node that is an ancestor of
        both u and v. A node is considered an ancestor of itself, so if one query
        node lies on the path from the root to the other, that node is returned.

        Args:
            u: First node.
            v: Second node.

        Returns:
            The lowest common ancestor of u and v.

        Raises:
            IndexError: If either node is outside the valid range [0, n).

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        if not 0 <= u < self.n or not 0 <= v < self.n:
            raise IndexError("node is outside the tree")

        # Make u the deeper node.
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        # Lift u to the same depth as v.
        depth_difference = self.depth[u] - self.depth[v]
        u = self._lift(u, depth_difference)

        if u == v:
            return u

        # Lift both nodes upward while their ancestors differ.
        for j in range(self.LOG - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]

        # They are now distinct children of the LCA.
        return self.up[u][0]

    def _lift(self, node: int, distance: int) -> int:
        """
        Move a node upward by a fixed number of edges.

        This helper assumes the requested move stays within the rooted tree and
        that node has already been validated by the public caller.

        Args:
            node: Node to move upward.
            distance: Number of edges to move toward the root.

        Returns:
            The ancestor reached after moving upward by distance edges.

        Complexity:
            Time: O(log n)
            Space: O(1)
        """
        bit = 0

        while distance:
            if distance & 1:
                node = self.up[node][bit]

            distance >>= 1
            bit += 1

        return node

    def distance(self, u: int, v: int) -> int:
        """
        Return the number of edges on the path between two nodes.

        The distance is computed from depths and the lowest common ancestor:

            depth[u] + depth[v] - 2 * depth[lca(u, v)]

        Args:
            u: First node.
            v: Second node.

        Returns:
            Number of edges in the unique tree path between u and v.

        Raises:
            IndexError: If either node is outside the valid range [0, n).

        Complexity:
            Time: O(log n), because it calls lca.
            Space: O(1)
        """
        ancestor = self.lca(u, v)

        return (
            self.depth[u]
            + self.depth[v]
            - 2 * self.depth[ancestor]
        )
