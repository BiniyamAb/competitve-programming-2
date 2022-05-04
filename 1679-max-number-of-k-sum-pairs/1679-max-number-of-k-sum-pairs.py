class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        op, l, r = 0, 0, len(nums)-1
        while l<r:
            sum = nums[l] + nums[r]
            if sum == k:
                l, r = l + 1, r - 1
                op+=1
            elif sum > k:r-=1
            else: l+=1
    
        return op
    