class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()

        def bin_search(ind,end):
            l,r,best = ind+1, len(rides)-1,len(rides)
            while l <= r:
                mid = l + (r-l)//2
                if rides[mid][0] >= end:
                    best = mid
                    r = mid-1
                else: l = mid + 1
                    
            return best

        @lru_cache(None)
        def dp(ind):
            if ind == len(rides): return 0
            start, end, tip = rides[ind]
            earning = (end - start) + tip
            best = bin_search(ind,end)
        
            pick = earning + dp(best)
            not_pick = dp(ind+1)

            return max(pick, not_pick)

        return dp(0)
