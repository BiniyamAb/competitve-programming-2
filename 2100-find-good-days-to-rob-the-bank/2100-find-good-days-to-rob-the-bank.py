class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time == 0: return range(len(security))
        increasing = decreasing = 1
        good_set, good_days = set(), []
        
        for i in range(1,len(security)-time):
            if i < len(security)-time and i >= time and increasing >= time and security[i-1] >= security[i]: good_set.add(i)
            if security[i-1] >= security[i]: increasing += 1
            else: increasing = 1
        
        for i in range(len(security)-2,time-1,-1):
            if i in good_set and decreasing >= time and security[i] <= security[i+1]: good_days.append(i)
            if security[i] <= security[i+1]: decreasing += 1
            else: decreasing = 1
            
        return good_days
                
                