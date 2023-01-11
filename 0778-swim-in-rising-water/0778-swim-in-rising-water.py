class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        inBound = lambda x, y: 0 <= x < n and 0 <= y < n
        DIR = (-1,0,1,0,-1)
        
        visited = {(0,0)}
        heap = [(grid[0][0],0,0)]
        
        while heap:
            time, row, col = heapq.heappop(heap)
            if row == col == n-1:
                return max(time, grid[row][col])
            
            for i in range(4):
                new_row, new_col = row + DIR[i], col + DIR[i+1]
                if inBound(new_row,new_col) and (new_row,new_col) not in visited:
                    curr_time = max(time, grid[new_row][new_col])
                    visited.add((new_row,new_col))
                    heapq.heappush(heap, (curr_time, new_row, new_col))
        
            
        
        
        