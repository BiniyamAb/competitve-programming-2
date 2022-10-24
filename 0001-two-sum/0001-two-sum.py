class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        target = 9
        [2,7,11,15]
              
        
        
        differences = {7:2}
        """
        differences = {}
        for i,num in enumerate(nums):
            if num in differences:
                return [differences[num], i]
            difference = target - num
            differences[difference] = i
        
        
        