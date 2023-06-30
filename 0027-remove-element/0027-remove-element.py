class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        l, r = 0, length - 1
        
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                l += 1
        
        return r + 1
            
        