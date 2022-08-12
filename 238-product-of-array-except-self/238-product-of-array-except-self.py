class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        def prefix(start,end,diff):
            prefix_sum = nums[0] if diff == 1 else nums[-1]
            for i in range(start,end,diff):
                answer[i] = prefix_sum * answer[i]
                prefix_sum*=nums[i]
        
        prefix(1,len(nums),1)
        prefix(len(nums)-2,-1,-1)
        
        return answer
                
            
        