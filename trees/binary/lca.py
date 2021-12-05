class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def find_lca(node, src, dst):
    if node is None: return None      
    if node.val in [src,dst]: return node        
    left = find_lca(node.left, src, dst)
    right = find_lca(node.right, src, dst)        
    if left and right: return node        
    if left: return left        
    return right