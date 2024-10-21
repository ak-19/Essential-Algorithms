class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        # Initialize the segment tree with zeros
        self.tree = [0] * (4 * self.n)
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

    def update(self, index, value, start, end, node):
        if start == end:
            # Update the leaf node
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                # Update the left child
                self.update(index, value, start, mid, 2 * node)
            else:
                # Update the right child
                self.update(index, value, mid + 1, end, 2 * node + 1)
            # Update the current node
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, l, r, start, end, node):
        if r < start or l > end:
            # No overlap
            return 0
        if l <= start and end <= r:
            # Total overlap
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        left_sum = self.query(l, r, start, mid, 2 * node)
        right_sum = self.query(l, r, mid + 1, end, 2 * node + 1)
        return left_sum + right_sum

data = [1, 3, 5, 7, 9, 11]

st = SegmentTree(data)
print(st.query(1, 3, 0, st.n - 1, 1))  # Output: 15

st.update(2, 6, 0, st.n - 1, 1)
print(st.query(1, 3, 0, st.n - 1, 1))  # Output: 16
