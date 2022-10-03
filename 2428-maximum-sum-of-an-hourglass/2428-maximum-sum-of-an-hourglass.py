class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        mx = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                top = grid[row][col] + grid[row][col+1] + grid[row][col+2]
                middle = grid[row+1][col+1]
                bottom = grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]
                mx = max(mx,top+middle+bottom)
        
        return mx
        