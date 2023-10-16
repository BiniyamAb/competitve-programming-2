"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        def recur(node):
            if node.child:
                node.child.prev = node
                tail = recur(node.child)
                tail.next = node.next
                if node.next: node.next.prev = tail
                node.next = node.child
                node.child = None
                return recur(tail)
            elif node.next:
                return recur(node.next)
            
            return node
        
        recur(head)
        return head
        