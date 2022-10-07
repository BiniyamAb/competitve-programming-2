class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        sum = left = 0
        for i in range(firstLen-1): sum += nums[i]
        max_sum = 0
        for i in range(firstLen-1,len(nums)):
            sum += nums[i]
            second_sum = second_left = 0
            for z in range(secondLen-1): second_sum += nums[z]
            second_max_sum = 0
            for j in range(secondLen-1,len(nums)):
                second_sum += nums[j]
                if j < left or second_left > i:
                    second_max_sum = max(second_max_sum,second_sum)
                second_sum -= nums[second_left]
                second_left += 1
            
            max_sum = max(max_sum, sum + second_max_sum)
            sum -= nums[left]
            left += 1
        
        return max_sum
            
                
            
            
            