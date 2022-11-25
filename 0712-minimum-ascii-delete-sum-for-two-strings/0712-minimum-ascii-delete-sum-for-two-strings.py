class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        
        @cache
        def dp(i, j):
            if i >= N or j >= M: return 0
            
            if s1[i] == s2[j]:
                return (ord(s1[i]) * 2) + dp(i + 1, j + 1)
            
            return max(dp(i + 1, j), dp(i, j + 1))
        
        total = 0
        for s in s1: total += ord(s)
        for s in s2: total += ord(s)
        
        return total - dp(0, 0)