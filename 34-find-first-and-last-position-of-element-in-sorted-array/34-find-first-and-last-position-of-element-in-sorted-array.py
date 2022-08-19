class Solution:
    def binarySearch(self,nums,target,length,flag):
        left = 0
        right = length - 1
        best = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                best = mid
                if flag:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return best
                
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        left_most = self.binarySearch(nums,target,length,True)
        right_most = self.binarySearch(nums,target,length,False)
        
        return [left_most,right_most]
        
        