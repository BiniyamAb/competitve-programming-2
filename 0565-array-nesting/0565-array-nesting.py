class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        longest = 1
        for num in nums:
            count = 0
            while num not in visited:
                visited.add(num)
                num = nums[num]
                count += 1
            longest = max(longest,count)
        
        return longest
    
        