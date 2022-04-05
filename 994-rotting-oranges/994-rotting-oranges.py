class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIR = (-1,0,1,0,-1)
        inBound = lambda r, c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        queue = deque()
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i,j))
                    
        minute = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                for i in range(4):
                    newRow, newCol = row + DIR[i], col + DIR[i+1]
                    if inBound(newRow, newCol) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        fresh.remove((newRow, newCol))
                        queue.append((newRow, newCol))
            minute+=1
            
        if fresh: return -1
        return 0 if minute == 0 else minute-1
        
        
        
        