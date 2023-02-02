class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        steps = len(count)
        if count[0] > 0:
            steps -= 1
        
        return steps