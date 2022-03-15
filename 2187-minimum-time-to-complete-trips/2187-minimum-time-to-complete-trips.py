class Solution:
    def summ(self, x, time):
        return sum(x//t for t in time)
        
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, min(time) * totalTrips
        best = r
        
        while l <= r:
            mid = l + (r-l)//2
            if self.summ(mid, time) >= totalTrips:
                best = mid
                r = mid - 1 
            else:
                l = mid + 1
        
        return best
            