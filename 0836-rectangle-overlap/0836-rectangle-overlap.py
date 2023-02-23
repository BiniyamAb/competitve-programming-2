class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:        
        
        first_intersect = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        second_intersect = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
                
        return first_intersect and second_intersect
                