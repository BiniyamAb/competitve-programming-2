class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        one_present = False
        for i in range(len(matrix)):
            one_present = "1" in matrix[i]
            if one_present: break
        if not one_present: return 0

        m, n = len(matrix), len(matrix[0])
        size = [[0 for j in range(n)] for i in range(2)]
        max_size = 1

        for j in range(n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            max_size = max(max_size, size[0][j])

        for i in range(1, m):
            if matrix[i][0] == '1':
                size[i % 2][0] = 1
            else:
                size[i % 2][0] = 0
            for j in range(1, n):
                if matrix[i][j] == '1':
                    size[i % 2][j] = min(size[i % 2][j - 1], size[(i - 1) % 2][j], size[(i - 1) % 2][j - 1]) + 1
                    max_size = max(max_size, size[i % 2][j])
                else:
                    size[i % 2][j] = 0

        return max_size * max_size