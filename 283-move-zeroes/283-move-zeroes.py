class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = zeros = n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pointer] = nums[i]
                pointer+=1
            else: zeros+=1
        
        for j in range(len(nums)-1, len(nums) - zeros - 1, -1): nums[j] = 0
        