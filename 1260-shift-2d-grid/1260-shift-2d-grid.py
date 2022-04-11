class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        def reverse(lo: int, hi: int) -> None:
            while lo < hi:
                r, c, i, j = lo // cols, lo % cols, hi // cols, hi % cols
                grid[r][c], grid[i][j] = grid[i][j], grid[r][c]
                lo += 1
                hi -= 1

        rows, cols = len(grid), len(grid[0])
        k %= rows * cols
        reverse(0, rows * cols - 1)
        reverse(0, k - 1)
        reverse(k, rows * cols - 1)
        return grid
        
        
        