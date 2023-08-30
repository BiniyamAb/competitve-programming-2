class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0
        
        for i in range(len(nums) - 2, -1, -1):
            curr_op = math.ceil(nums[i] / nums[i+1]) - 1
            op += curr_op

            elem = math.ceil(nums[i] / nums[i+1])
            num  = nums[i] // elem
            
            nums[i] = num
        
        return op
        