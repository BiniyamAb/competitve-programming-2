class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        length = len(s)
        for st in t:
            if s_pointer == length: 
                break
            
            if st == s[s_pointer]:
                s_pointer += 1
        
        return s_pointer == length
                
                
        