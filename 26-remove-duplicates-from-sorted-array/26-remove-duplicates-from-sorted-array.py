class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[l] and nums[i] > nums[l]:
                l+=1
                nums[i], nums[l] = nums[l], nums[i]
        
        return l+1
            
        