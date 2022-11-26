class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        
        sum = maxx = nums[0]
        for num in nums[1:]:
            sum = max(num, sum + num)
            maxx = max(maxx, sum)

        return maxx
        