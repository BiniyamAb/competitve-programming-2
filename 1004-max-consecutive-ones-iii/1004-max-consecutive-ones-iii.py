class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = l = 0
        for i in range(len(nums)):
            if nums[i] != 1 and k > 0:
                k-=1
            elif nums[i] != 1:
                max_ones = max(max_ones, i - l)
                while k == 0:
                    if nums[l] == 0: k += 1
                    l+=1
                k-=1
        return max(max_ones, i - l + 1)