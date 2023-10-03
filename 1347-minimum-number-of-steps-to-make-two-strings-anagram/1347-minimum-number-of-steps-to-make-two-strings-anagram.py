class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        
        min_steps = 0
        
        for key, value in s_count.items():
            if key in t_count:
                diff =  max(0, value - t_count[key])
            else: diff = value
            
            min_steps += diff
        
        return min_steps
                
        