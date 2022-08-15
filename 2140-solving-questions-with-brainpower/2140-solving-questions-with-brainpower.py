class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        inBound = lambda i: 0 <= i < len(questions)
        
        @cache
        def dp(ind):
            if not inBound(ind): return 0
            points, brain_power = questions[ind]
            pick = dp(ind+brain_power+1) + points
            not_pick = dp(ind+1)
            
            return max(pick,not_pick)
        
        return dp(0)
            
        