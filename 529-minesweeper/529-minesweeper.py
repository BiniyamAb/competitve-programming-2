class Solution:
    def adjacentMines(self, row, col, board):
        mines = 0
        for i in range(8):
            newRow, newCol = row + self.DIR[i], col + self.DIR[i+1]
            if self.inBound(newRow, newCol) and board[newRow][newCol] == 'M':
                mines+=1
                
        return mines if mines > 0 else -1
    
    def dfs(self, row, col, board):
        mines = self.adjacentMines(row, col, board)
        if mines > 0:
            board[row][col] = str(mines)
            return
        
        board[row][col] = "B"
        for i in range(8):
            newRow, newCol = row + self.DIR[i], col + self.DIR[i+1]
            if self.inBound(newRow, newCol) and board[newRow][newCol] == "E":
                self.dfs(newRow, newCol, board)
    
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.inBound = lambda row, col: 0 <= row < len(board) and 0 <= col < len(board[0])
        self.DIR = (-1,0,1,0,-1,-1,1,1,-1)
        
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        
        self.dfs(click[0], click[1], board)
        
        return board
        