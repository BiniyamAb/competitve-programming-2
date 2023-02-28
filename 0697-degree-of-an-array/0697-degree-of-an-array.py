class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        degree = max(count.values())
        if degree == 1: return 1
        indexes = defaultdict(list)
        for i in range(len(nums)):
            num = nums[i]
            if count[num] == degree:
                if len(indexes[num]) > 1: indexes[num].pop()
                indexes[num].append(i)
                
        smallest = len(nums)
        for k, v in indexes.items():
            smallest = min(smallest, v[-1] - v[0] + 1)
        
        return smallest
            