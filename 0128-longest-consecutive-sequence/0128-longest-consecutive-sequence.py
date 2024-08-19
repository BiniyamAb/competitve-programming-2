class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in nums:
            if num-1 in numSet: continue
            curr_length = 1
            while num + 1 in numSet:
                curr_length += 1
                num += 1
            
            longest = max(longest, curr_length)
        
        return longest

