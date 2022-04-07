class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            if x == y:
                continue
            else: 
                heapq.heappush(stones, -abs(y-x))
                
        return -stones[0] if len(stones) > 0 else 0 