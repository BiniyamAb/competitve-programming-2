class Solution:
    @cache
    def getPowerValue(self, x):
        if x == 1: 
            return 0
        
        if x % 2 == 0:
            return self.getPowerValue(x // 2) + 1
        
        return self.getPowerValue((x * 3) + 1) + 1
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_val = {}
        nums = [i for i in range(lo,hi+1)]
        for num in nums:
            curr_power_val = self.getPowerValue(num)
            power_val[num] = curr_power_val
        
        nums.sort(key=lambda num: (power_val[num], num))
        return nums[k-1]
        