class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        
        @cache
        def dp(i, j):
            if i >= N: 
                return M - j
            
            if j >= M: 
                return N - i
            
            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)
            
            insert = dp(i, j + 1)
            replace = dp(i + 1, j + 1)
            delete = dp(i + 1, j)
            
            return min(insert, delete, replace) + 1
        
        return dp(0, 0)