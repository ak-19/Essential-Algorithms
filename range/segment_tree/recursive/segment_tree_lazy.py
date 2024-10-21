class SegmentTreeLazy:
    def __init__(self, data):
        self.n = len(data)
        # Initialize the segment tree and lazy tree with zeros
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build_tree(data, 0, self.n - 1, 1)

    def build_tree(self, data, start, end, node):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            # Build left and right subtrees
            self.build_tree(data, start, mid, 2 * node)
            self.build_tree(data, mid + 1, end, 2 * node + 1)
            # Combine the results
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def update_range(self, l, r, val, start, end, node):
        # Check for pending updates and apply them
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                # Propagate to children
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        # No overlap
        if r < start or l > end:
            return

        # Total overlap
        if l <= start and end <= r:
            self.tree[node] += (end - start + 1) * val
            if start != end:
                # Mark children as lazy
                self.lazy[2 * node] += val
                self.lazy[2 * node + 1] += val
            return

        # Partial overlap
        mid = (start + end) // 2
        self.update_range(l, r, val, start, mid, 2 * node)
        self.update_range(l, r, val, mid + 1, end, 2 * node + 1)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query_range(self, l, r, start, end, node):
        # Check for pending updates and apply them
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                # Propagate to children
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

        # No overlap
        if r < start or l > end:
            return 0

        # Total overlap
        if l <= start and end <= r:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2
        left_sum = self.query_range(l, r, start, mid, 2 * node)
        right_sum = self.query_range(l, r, mid + 1, end, 2 * node + 1)
        return left_sum + right_sum

data = [1, 3, 5, 7, 9, 11]
st = SegmentTreeLazy(data)

print("Initial sum of elements 1 to 3:", st.query_range(1, 3, 0, st.n - 1, 1))  # Output: 15
st.update_range(1, 3, 10, 0, st.n - 1, 1)

print("Sum of elements 1 to 3 after range update:", st.query_range(1, 3, 0, st.n - 1, 1))  # Output: 45
print("Total sum after range update:", st.query_range(0, 5, 0, st.n - 1, 1))  # Output: 66
