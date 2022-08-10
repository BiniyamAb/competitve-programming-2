# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heapq.heappush(merged, head.val)
                head = head.next
        if not len(merged) > 0:
            return None
        head = temp = ListNode(val = heapq.heappop(merged))
        while len(merged) > 0:
            temp.next = ListNode(val = heapq.heappop(merged))
            temp = temp.next
        
        return head
            
        
        