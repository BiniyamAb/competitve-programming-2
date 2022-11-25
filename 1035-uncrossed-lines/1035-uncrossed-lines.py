class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        N, M = len(nums1), len(nums2)
        
        @cache
        def dp(i, j):
            if i >= N or j >= M: return 0
            
            if nums1[i] == nums2[j]:
                return 1 + dp(i + 1, j + 1)
            
            return max(dp(i + 1, j), dp(i, j + 1))
        
        return dp(0, 0)