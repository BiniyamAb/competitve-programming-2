class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        r_sum, l_sum = sum(nums) - nums[0], 0
        for i in range(len(nums)-1):
            if r_sum == l_sum: return i
            l_sum, r_sum = l_sum + nums[i], r_sum - nums[i+1]
        if r_sum == l_sum: return len(nums)-1
        return -1
        
        