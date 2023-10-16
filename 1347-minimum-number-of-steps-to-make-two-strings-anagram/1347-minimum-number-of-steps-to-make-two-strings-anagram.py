class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s) 
        t_count = Counter(t)
        
        steps = 0
        for k in t_count:
            steps += max(0, t_count[k] - s_count[k])
        
        return steps