class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    prev = None
    while head:
        head.next, prev = prev, head.next
        if prev: prev.next, head = head, prev.next
        else: prev, head = head, prev   
    
    return prev

head = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
