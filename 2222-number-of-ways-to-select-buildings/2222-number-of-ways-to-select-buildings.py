class Solution:
    def numberOfWays(self, s: str) -> int:
        ways = 0
        seen = [[0] * 2 for i in range(2)]
        
        for i in range(len(s)):
            char = int(s[i])
            ways += seen[1][1-char]
            seen[1][char] += seen[0][1-char]
            seen[0][char] += 1
            
        return ways