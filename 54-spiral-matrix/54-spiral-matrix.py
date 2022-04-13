class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col, count, res = 0, 0, float("inf"), []
        inBound = lambda r, c: 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
        while count > 0:
            count = 0
            while inBound(row, col) and matrix[row][col] != "#":
                res.append(matrix[row][col])
                matrix[row][col] = "#"
                count+=1
                col+=1
            row, col = row + 1, col - 1
            while inBound(row, col) and matrix[row][col] != "#":
                res.append(matrix[row][col])
                matrix[row][col] = "#"
                count+=1
                row+=1
            row, col = row - 1, col - 1
            while inBound(row, col) and matrix[row][col] != "#":
                res.append(matrix[row][col])
                matrix[row][col] = "#"
                count+=1
                col-=1
            row, col = row - 1, col + 1
            while inBound(row, col) and matrix[row][col] != "#":
                res.append(matrix[row][col])
                matrix[row][col] = "#"
                row-=1
            row, col = row + 1, col + 1
        
        return res
        