# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap =  []
        head = merged = ListNode()
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(heap,(node.val,i,node))
        
        while heap:
            val, i, node = heapq.heappop(heap)
            head.next = node
            head = head.next
            if node.next:
                node = node.next
                heapq.heappush(heap,(node.val,i,node))
        
        
        return merged.next
            