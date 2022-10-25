class Solution:
    def longestPrefix(self, s: str) -> str:
        LPS = [0] * len(s)
        pointer = 0
        for i in range(1,len(s)):
            while pointer != 0 and s[pointer] != s[i]:
                pointer = LPS[pointer-1]
            if s[i] == s[pointer]:
                LPS[i] = pointer + 1
                pointer += 1
        
        return s[:LPS[-1]]
            