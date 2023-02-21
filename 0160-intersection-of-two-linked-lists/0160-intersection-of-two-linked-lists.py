# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def findLength(node):
            count = 0
            while node:
                node = node.next
                count += 1
                
            return count
        
        lengthA = findLength(headA)
        lengthB = findLength(headB)
        
        diff = abs(lengthA - lengthB)
        if lengthA < lengthB:
            headA, headB = headB, headA
            
        for _ in range(diff): headA = headA.next
            
        for _ in range(min(lengthA,lengthB)):
            if headA == headB: return headA
            headA = headA.next
            headB = headB.next
        
        return None
            
        
        
        
        
        