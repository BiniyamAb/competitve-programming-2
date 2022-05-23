class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        for i in range(len(strs)):
            zero = one = 0
            binary = strs[i]
            for s in binary:
                if s == '0': zero+=1
                else: one+=1
            strs[i] = (zero,one)
        
        @lru_cache(None)
        def dp(i,j,idx):
            if i<0 or j<0:
                return -math.inf
            
            if idx==len(strs):
                return 0
            
            return max(dp(i,j,idx+1), 1 + dp(i-strs[idx][0], j-strs[idx][1], idx+1))
        
        return dp(m,n,0)