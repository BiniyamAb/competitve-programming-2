class NumMatrix:

    def __init__(self, matrix: List[List[int]]):   
        self.matrix = matrix
        temp = [0] * (len(self.matrix[0]) + 1)
        self.matrix.append(temp)

        for i in range(len(matrix)-1):
            self.matrix[i].append(0)
            for j in range(len(matrix[i])-1):
                self.matrix[i][j] += self.calculatePrefix(i,j,i,j)
    
    def calculatePrefix(self,r,c,r2,c2):
        upper = self.matrix[r-1][c2]
        left = self.matrix[r2][c-1]
        upperleft = self.matrix[r-1][c-1]
        
        return upper + left - upperleft

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:              
        return self.matrix[row2][col2] - self.calculatePrefix(row1,col1,row2,col2)
        
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)