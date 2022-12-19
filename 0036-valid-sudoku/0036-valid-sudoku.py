class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_set = [set() for _ in range(9)]
        row_set = [set() for _ in range(9)]
        grid_set = [set() for _ in range(9)]
        for r in range(9):
            add = (r//3) * 3
            for c in range(9):
                num = board[r][c]
                if num.isdigit():
                    if num in row_set[r] or num in column_set[c] or num in grid_set[(c//3) + add]:
                        return False
                    row_set[r].add(num)
                    column_set[c].add(num)
                    grid_set[(c//3) + add].add(num)
                    
        return True 