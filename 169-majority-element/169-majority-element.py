class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq, n = Counter(nums), len(nums)
        for k, v in freq.items():
            if v > n//2: return k