class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            if len(heap) == k: heapq.heappushpop(heap, nums[i])
            else: heapq.heappush(heap, nums[i])
                
        return heap[0]