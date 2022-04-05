class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0
        
        while l < r:
            newArea = min(height[l], height[r]) * (r - l)
            area = max(area, newArea)
            if height[l] > height[r]:
                r-=1
            else:
                l+=1
        
        return area
