class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        longest = 1
        for i in range(len(nums)):
            if nums[i]-1 in nums_set: continue
            count = 1
            num = nums[i]+1
            while num in nums_set:
                count+=1
                num+=1
            longest = max(longest,count)
        
        return longest
            