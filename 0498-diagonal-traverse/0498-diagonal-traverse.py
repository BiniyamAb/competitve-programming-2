class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal_list = []
        inBound = lambda row, col: 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
        def traverseDiagonal(row, col, reverse):
            curr_diagonal_list = []
            while inBound(row,col):
                curr_diagonal_list.append(mat[row][col])
                row, col = row - 1, col + 1
            
            if reverse: curr_diagonal_list.reverse()
            return curr_diagonal_list
        
        reverse = False
        for i in range(len(mat)):
            curr_diagonal_list = traverseDiagonal(i,0,reverse)
            diagonal_list.extend(curr_diagonal_list)
            reverse = not reverse
        
        for i in range(1,len(mat[0])):
            curr_diagonal_list = traverseDiagonal(len(mat)-1,i,reverse)
            diagonal_list.extend(curr_diagonal_list)
            reverse = not reverse
        
        return diagonal_list
            
                
        