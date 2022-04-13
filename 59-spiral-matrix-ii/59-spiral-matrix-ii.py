class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n) ]
        row, col, count, num = 0, 0, float("inf"), 1
        inBound = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        while count > 0:
            count = 0
            while inBound(row, col) and matrix[row][col] == 0:
                matrix[row][col] = num
                count, num = count + 1, num + 1
                col+=1
            row, col = row + 1, col - 1
            while inBound(row, col) and matrix[row][col] == 0:
                matrix[row][col] = num
                count, num = count + 1, num + 1
                row+=1
            row, col = row - 1, col - 1
            while inBound(row, col) and matrix[row][col] == 0:
                matrix[row][col] = num
                count, num = count + 1, num + 1
                col-=1
            row, col = row - 1, col + 1
            while inBound(row, col) and matrix[row][col] == 0:
                matrix[row][col] = num
                count, num = count + 1, num + 1
                row-=1
            row, col = row + 1, col + 1
        
        return matrix