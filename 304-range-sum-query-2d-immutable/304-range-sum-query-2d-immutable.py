class NumMatrix:

    def __init__(self, matrix: List[List[int]]):   
        self.matrix = matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.matrix[i][j] += self.calculatePrefix(i,j)
        
        print(self.matrix)
    
    def calculatePrefix(self,r,c):
        upper = left = upperleft = 0
        if r != 0: upper = self.matrix[r-1][c]
        if c != 0: left = self.matrix[r][c-1]
        if c != 0 and r != 0: upperleft = self.matrix[r-1][c-1]
        
        return upper + left - upperleft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:  
        upper = left = upperleft = 0
        if row1 != 0: upper = self.matrix[row1-1][col2]
        if col1 != 0: left = self.matrix[row2][col1-1]
        if col1 != 0 and row1 != 0: upperleft = self.matrix[row1-1][col1-1]
            
        return self.matrix[row2][col2] - (upper + left - upperleft)
        
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)