class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        memo = {}
        inBound = lambda x: 0 <= x < len(nums)
        def dp(i):
            if memo.get(i) is not None: return memo[i]
            maxx = 0
            ind = i + 2
            while inBound(ind):
                maxx = max(maxx, dp(ind))
                ind+=1
            
            memo[i] = maxx + nums[i]
            return memo[i]       
        
        
        return max(dp(0), dp(1))
        
        
            
        
        
        