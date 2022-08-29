class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            if heights[i] >= heights[i+1]:
                continue
            dif = heights[i+1] - heights[i]
            if len(heap) < ladders:
                heapq.heappush(heap, (dif,i,i+1))
            else:
                small = heapq.heappushpop(heap, (dif,i,i+1))
                if small[0] <= bricks:
                    bricks-=small[0]
                else:
                    return i
        return len(heights) - 1