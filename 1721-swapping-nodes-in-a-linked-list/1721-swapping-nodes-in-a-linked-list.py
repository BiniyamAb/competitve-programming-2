# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = head
        for i in range(k-1):
            fast = fast.next
        change = fast
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        change.val, slow.val = slow.val, change.val
        return head
        