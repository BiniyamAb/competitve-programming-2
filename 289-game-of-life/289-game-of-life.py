class Solution:
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        DIR = (1,0,-1,0,1,1,-1,-1,1)
        inBound = lambda r, c: 0 <= r < len(board) and 0 <= c < len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])): board[i][j] = [board[i][j], 0]
        
        def dfs(row, col, board):
            visited.add((row,col))
            live = 0
            for i in range(8):
                newRow, newCol = row + DIR[i], col + DIR[i+1]
                if inBound(newRow, newCol) and (newRow,newCol) not in visited:
                    live += dfs(newRow, newCol, board)
                elif inBound(newRow, newCol):
                    live += board[newRow][newCol][0]
                    
            if board[row][col][0] == 1 and (live > 3 or live < 2): board[row][col][1] = 0
            elif board[row][col][0] == 0 and live == 3: board[row][col][1] = 1
            else: board[row][col][1] = board[row][col][0]
            return board[row][col][0]
        
        dfs(0, 0, board)
        for i in range(len(board)): 
            for j in range(len(board[0])): board[i][j] = board[i][j][1]
        
        
                
        
        