class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        l = 0
        r = N - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if mid % 2 == 0:
                if 0 < mid < (N - 1):
                    if nums[mid] == nums[mid+1]: l = mid + 1
                    elif nums[mid] == nums[mid-1]: r = mid - 1
                    else: return nums[mid]
                else: return nums[mid]
                
            else:
                if 0 < mid < (N - 1):
                    if nums[mid] == nums[mid+1]: r = mid - 1 
                    elif nums[mid] == nums[mid-1]: l = mid + 1
                    else: return nums[mid]
                else: return nums[mid]
        