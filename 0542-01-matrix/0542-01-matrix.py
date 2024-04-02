class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    continue
                matrix[i][j] = float("inf")
                if i > 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i-1][j]+1)
                if j > 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i][j-1]+1)
        for i in reversed(range(len(matrix))):
            for j in reversed(range(len(matrix[i]))):
                if not matrix[i][j]:
                    continue
                if i < len(matrix)-1:
                    matrix[i][j] = min(matrix[i][j], matrix[i+1][j]+1)
                if j < len(matrix[i])-1:
                    matrix[i][j] = min(matrix[i][j], matrix[i][j+1]+1)
        return matrix