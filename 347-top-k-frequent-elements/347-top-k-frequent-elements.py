class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for key, v in freq.items():
            if len(heap) < k: heapq.heappush(heap, (v,key))
            else: heapq.heappushpop(heap, (v,key))
        
        for i in range(len(heap)): heap[i] = heap[i][1]
        
        return heap
        