class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostK(nums, k):
            count = defaultdict(int)
            l = r = res = 0
            while r < len(nums):
                count[nums[r]] += 1
                r += 1
                while l < r and len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        count.pop(nums[l])
                    l += 1
                
                res += r - l
                
            return res
        
        res = (atMostK(nums, k) - atMostK(nums, k-1))
        return res