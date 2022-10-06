class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maximum_consecutives = 0
        for i in range(len(nums)):                    
            
            if nums[i] == 0 and k == 0:
                maximum_consecutives = max(maximum_consecutives,i-l)  
                while k == 0:
                    k += 1 - nums[l]
                    l+=1
                
            if nums[i] == 0:
                k-=1
                
        maximum_consecutives = max(maximum_consecutives,i-l+1)  
        
        return maximum_consecutives
        