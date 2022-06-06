# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        root = head
        head = prev = ListNode(-101,root)     
        while root and root.next:
            looped = False
            while root.next and root.val == root.next.val: 
                root.next = root.next.next
                looped = True
            if looped:
                prev.next = root.next
                root = prev
                
            prev = root
            root = root.next
        
        return head.next
            
        