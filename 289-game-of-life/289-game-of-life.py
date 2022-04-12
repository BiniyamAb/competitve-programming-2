class Solution:
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited, grid = set(), []
        DIR = (1,0,-1,0,1,1,-1,-1,1)
        inBound = lambda r, c: 0 <= r < len(board) and 0 <= c < len(board[0])
        for i in range(len(board)):
            lst = []
            for j in range(len(board[0])):lst.append(0)
            grid.append(lst)
        
        def dfs(row, col, board):
            visited.add((row,col))
            live = 0
            for i in range(8):
                newRow, newCol = row + DIR[i], col + DIR[i+1]
                if inBound(newRow, newCol) and (newRow,newCol) not in visited:
                    live += dfs(newRow, newCol, board)
                elif inBound(newRow, newCol):
                    live += board[newRow][newCol]
                    
            if board[row][col] == 1 and (live > 3 or live < 2): grid[row][col] = 0
            elif board[row][col] == 0 and live == 3: grid[row][col] = 1
            else: grid[row][col] = board[row][col]
            return board[row][col]
        
        dfs(0, 0, board)
        for i in range(len(grid)): 
            for j in range(len(grid[0])): board[i][j] = grid[i][j]
        
        
                
        
        