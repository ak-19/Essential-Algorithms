def detectCycle(head):
    '''If exists, find cycle node in linked list'''
    def get_node():
        fast = slow = head        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next            
            if fast == slow: return slow
        return None
    
    node = get_node()
        
    if node is None: return None
    
    while node != head:            
        node = node.next
        head = head.next
        
    return node

def detectCycleHashing(head):
    visited = set()
    node = head
    while node:            
        if node in visited: return node
        visited.add(node)
        node = node.next                                    
    return None