class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minn = nums[0]
        diff = float("-inf")
        for i in range(1,len(nums)):
            diff = max(diff, nums[i] - minn)
            minn = min(minn, nums[i])
        
        if diff <= 0: return -1
        return diff
            
        