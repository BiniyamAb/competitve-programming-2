class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        score = 0
        for _ in range(k):
            num = -heappop(nums)
            score += num
            num = math.ceil(num/3)
            heappush(nums,-num)
        
        return score