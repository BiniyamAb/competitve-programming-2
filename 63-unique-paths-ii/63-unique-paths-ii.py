class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1: return 0
        inBound = lambda r,c: 0 <= r < len(obstacleGrid) and 0 <= c < len(obstacleGrid[0])
        
        @lru_cache(None)
        def dfs(row,col):
            if (row,col) == (len(obstacleGrid)-1, len(obstacleGrid[0])-1): return 1
            paths = 0
            for i,j in [(0,1),(1,0)]:
                nr, nc = row + i, col + j
                if inBound(nr,nc) and obstacleGrid[nr][nc] == 0:      
                    paths+=dfs(nr,nc)
            
            return paths
        
        return dfs(0,0)
        