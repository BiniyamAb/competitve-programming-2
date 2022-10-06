class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1: return False
        reminder_map = {0:-1}
        sum = 0
        for i,num in enumerate(nums):
            sum += num
            reminder = sum % k
            if reminder in reminder_map:
                if i - reminder_map[reminder] > 1: 
                    return True
            elif reminder not in reminder_map:
                reminder_map[reminder] = i

        return False