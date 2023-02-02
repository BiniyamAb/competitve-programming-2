class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        non_zero = []
        for num in nums:
            if num != 0: non_zero.append(num)
                
        if not non_zero: return 0
        non_zero.sort()
        steps = 1
        subtract_val = non_zero[0]
        for i in range(1,len(non_zero)):
            non_zero[i] -= subtract_val
            if non_zero[i] != 0:
                subtract_val += non_zero[i]
                steps += 1
        
        return steps
        