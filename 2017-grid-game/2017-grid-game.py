class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        if len(grid[0]) <= 1: return 0
        
        for i in range(1,len(grid[0])):
            grid[1][i] += grid[1][i-1]
        
        for i in range(len(grid[0])-2,-1,-1):
            grid[0][i] += grid[0][i+1]
        
        minn = min(grid[0][1], grid[1][-2])
        for i in range(1,len(grid[0])-1):
            curr = max(grid[0][i+1], grid[1][i-1])
            minn = min(minn, curr)
        
        return minn
        