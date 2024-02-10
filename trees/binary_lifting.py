from collections import defaultdict

#test purpses
def generate_tree_n_2_children(n):
    tree = defaultdict(list)
    for i in range(n):
        if 2*i+1 <= n: tree[i].append(2*i+1)
        if 2*i + 2 <= n: tree[i].append(2*i + 2)
    return tree

class BinaryLifter:
    '''Binary Lifting is a technique to find the kth ancestor of a node in a tree in O(logn) time.'''
    def __init__(self, tree, n) -> None:
        self.tree = tree
        self.n = n
        self.generate_binary_lifting_table()

    def generate_binary_lifting_table(self):
        dp = [[-1 for _ in range(8)] for _ in range(self.n+1)]    
        for i in range(self.n):
            for child in self.tree[i]: dp[child][0] = i
        for j in range(1, 8):
            for i in range(self.n+1):
                if dp[i][j-1] != -1:
                    dp[i][j] = dp[dp[i][j-1]][j-1]
        self.dp = dp

    def kth_ancestor(self, u, k):
        for i in range(8):
            if k & (1 << i): u = self.dp[u][i]
        return u
    