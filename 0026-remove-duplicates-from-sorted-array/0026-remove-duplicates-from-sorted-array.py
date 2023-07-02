class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        i = 1
        while i < len(nums):
            while i < len(nums) and nums[i] == nums[pointer]: i+=1
            
            if i < len(nums):
                nums[pointer+1] = nums[i]
                pointer += 1
                i += 1
        
        return pointer + 1
        