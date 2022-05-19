class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        DIR = (-1,0,1,0,-1)
        memo = {}
        inBound = lambda r,c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        
        @lru_cache(None)
        def dfs(row, col):
            length = 0
            for i in range(4):
                nr, nc = DIR[i] + row, DIR[i+1] + col
                if inBound(nr,nc) and matrix[nr][nc] > matrix[row][col]:
                    length = max(length,dfs(nr,nc))

            return length+1
        
        longest = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                longest = max(longest, dfs(r,c))
            
        return longest