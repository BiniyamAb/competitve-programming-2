class Solution:
    def combinations(self,ind,nums,combs,path,length,sum,high_bound):
        path.append(nums[ind])
        sum += nums[ind]
        if len(path) != length:
            for i in range(ind+1,len(nums)):
                self.combinations(i,nums,combs,path,length,sum,high_bound)
        else:
            if sum <= high_bound:
                combs.append(sum)
            
        path.pop()
        
        
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [1,2,4,8]
        minutes = [1,2,4,8,16,32]
        ans = set()
        for i in range(turnedOn+1):
            hour_combs = []
            minute_combs = []
            
            if i > 3 or turnedOn - i > 5: continue
                
            for j in range(4):
                self.combinations(j,hours,hour_combs,[],i,0,11)
            for j in range(6):
                self.combinations(j,minutes,minute_combs,[],turnedOn-i,0,59)
                
            if len(hour_combs) == 0: hour_combs = [0]
            if len(minute_combs)== 0: minute_combs = [0]
                
            for hour in hour_combs:
                hour = str(hour)
                for minute in minute_combs:
                    minute = str(minute)
                    if int(minute) <= 9: minute = "0" + minute
                    time = hour + ":" + minute
                    ans.add(time)                  
        
        return sorted(list(ans))
                            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            