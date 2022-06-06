# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        lst = []
        root = head
        while root:
            lst.append(root)
            root = root.next
        
        lst.sort(key=lambda x: x.val)
        head = root = lst[0]
        for i in range(1,len(lst)):
            root.next = lst[i] 
            root = root .next
        root.next = None
        return head