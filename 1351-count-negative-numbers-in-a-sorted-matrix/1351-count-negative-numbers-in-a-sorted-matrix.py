class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            l, r = 0, len(row) - 1
            best = -1
            while l <= r:
                mid = l + (r - l) // 2
                if row[mid] < 0:
                    best = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            if best != -1:
                count += len(row) - best
        
        return count
            
        
            
        