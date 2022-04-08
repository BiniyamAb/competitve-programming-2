class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        best = l = sum = 0
        for i in range(len(nums)):
            sum += nums[l] - nums[i]
            best = max(best, i-l)
            while sum > k and l < i:
                l+=1
                sum-= (nums[l-1]-nums[l]) * (i-l+1)
                    
        return max(best, i-l+1)
                
        