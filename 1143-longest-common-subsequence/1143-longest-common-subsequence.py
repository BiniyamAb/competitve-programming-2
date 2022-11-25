class Solution:
    def longestCommonSubsequence(self, A: str, B: str) -> int:
        N, M = len(A), len(B)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if A[j - 1] == B[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[M][N]