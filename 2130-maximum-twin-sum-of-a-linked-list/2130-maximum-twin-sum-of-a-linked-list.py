# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nodes, l, maxx = [], 0, 0
        while head:
            nodes.append(head.val)
            head = head.next
        
        while l < len(nodes):
            maxx = max(maxx, nodes[l]+nodes[-1])
            l+=1
            nodes.pop()
        
        return maxx
        