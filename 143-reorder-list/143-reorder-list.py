# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst = []
        while head:
            lst.append(head)
            head = head.next
        i, n = 1, len(lst)
        root = lst[0]
        while lst and i < len(lst)-1:
            root.next = lst.pop()
            root.next.next = lst[i]
            root = root.next.next
            i+=1
        
        if n%2 == 0: 
            root.next = lst[i]
            root = root.next
        root.next = None
        return head
        
            
        