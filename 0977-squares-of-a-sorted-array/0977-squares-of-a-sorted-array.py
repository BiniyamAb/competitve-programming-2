class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): nums[i] = nums[i] ** 2
        if len(nums) == 1: return nums
    
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res.append(left)
                l += 1
            else:
                res.append(right)
                r -= 1
                
        res.reverse()
        return res
