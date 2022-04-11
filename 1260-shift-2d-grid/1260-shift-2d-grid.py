class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        while k > 0:
            _next = grid[0][0]
            for i in range(m):
                for j in range(n):
                    if i == m - 1 and j == n - 1:
                        grid[0][0], _next = _next, grid[0][0] 
                    elif j == n - 1:
                        grid[i+1][0], _next = _next, grid[i+1][0]
                    else:
                        grid[i][j+1], _next = _next, grid[i][j+1]
            k-=1
        
        return grid
        
        
        