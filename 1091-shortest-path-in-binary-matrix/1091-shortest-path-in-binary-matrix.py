class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        n = len(grid)
        visited = set()
        DIR = (-1,0,1,0,-1,1,1,-1,-1)
        inBound = lambda row, col: 0 <= row < n and 0 <= col < n
        queue = deque([(0,0,1)])
        
        
        while queue:
            row, col, count = queue.popleft()
            if row == n - 1 and col == n - 1:
                return count
            for i in range(8):
                newRow, newCol = DIR[i] + row, DIR[i+1] + col
                if inBound(newRow, newCol) and grid[newRow][newCol] == 0 and (newRow, newCol) not in visited:
                    queue.append((newRow, newCol, count+1))
                    visited.add((newRow, newCol))
                    
        return -1
                