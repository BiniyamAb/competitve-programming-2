class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = {"a":0, "b":0, "c":0}
        l = 0
        count = 0
        length = len(s)
        for i in range(len(s)):
            abc[s[i]] += 1
            to_right = length - i
            while abc["a"] > 0 and abc["b"] > 0 and abc["c"] > 0 and l < i:
                count += to_right
                abc[s[l]] -= 1
                l+=1
        
        return count
                
            
        
        
        