class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        N = len(ranges)
        tap_intervals = []
        for i in range(N):
            if ranges[i] != 0:
                tap_intervals.append( (max(i-ranges[i], 0), min(i+ranges[i], N-1)) )
            
        tap_intervals.sort()
        
        N = len(tap_intervals)
        i = 0
        tap_opened = 0
        last = 0
        while i < N:
            temp = 0
            while i < N and tap_intervals[i][0] <= last:
                temp = max(temp, tap_intervals[i][1])
                i += 1
                
            if temp == 0: return -1
            if temp > last:
                last = temp
                tap_opened += 1
            
        
        if tap_opened == 0: return -1  
        if last < len(ranges)-1: return -1
        return tap_opened
            
        