class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r, length = 0, len(matrix) - 1, len(matrix[0]) - 1
        
        while row_l <= row_r:
            mid = row_l + (row_r - row_l)//2
            if matrix[mid][0] > target:
                row_r = mid - 1
            else:
                l, r = 0, length
                while l <= r:
                    mid2 = l + (r-l)//2
                    if matrix[mid][mid2] > target:
                        r = mid2 - 1
                    elif matrix[mid][mid2] == target:
                        return True
                    else:
                        l = mid2 + 1
                row_l = mid + 1
        
        return False
                
            