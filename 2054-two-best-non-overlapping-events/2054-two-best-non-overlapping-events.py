class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        def bin_search(ind,end):
            l,r,best = ind+1,len(events)-1,len(events)
            while l<=r:
                mid = l + (r-l)//2
                if events[mid][0] > end:
                    r = mid - 1
                    best = mid
                else: l = mid + 1
            
            return best
        
        @cache
        def dp(ind,count):
            if ind == len(events) or count == 2: return 0
            start, end, value = events[ind]
            best = bin_search(ind,end)
            
            pick = value + dp(best,count+1)
            not_pick = dp(ind+1,count)
            
            return max(pick, not_pick)
        
        return dp(0,0)