class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        n = len(s)
        steps = 0 
        s = list(s)
        while True:
            count = i = 1
            while i < n:
                if s[i] == "1" and s[i-1] == "0":
                    s[i], s[i-1] = "0", "1"
                    count += 1
                    i += 2
                else: i += 1
                
            if count > 1: steps += 1
            else: break
                
        return steps 
                
        
        
        