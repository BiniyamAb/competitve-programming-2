class Solution:
    def search(self, nums: List[int], target: int) -> int:       
        rotated = target > nums[-1] 
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r-l)//2
                
            if nums[mid] == target:
                return mid
            
            else:
                is_same_part = (nums[mid] > nums[-1] and rotated) or (nums[mid] <= nums[-1] and not rotated)
                if nums[mid] > target:
                    if is_same_part:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    if is_same_part:
                        l = mid + 1
                    else:
                        r = mid - 1

                
        return -1
            