class Solution:
    def counter(self,nums,current_number,length):
        count = 0
        for num in nums:
            if num <= current_number:
                count += 1
        
        return count
        
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        left = 1
        right = length - 1
        best = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            curr_count = self.counter(nums,mid,length)
            
            if curr_count > mid:
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        
        return best
        
        
            
        