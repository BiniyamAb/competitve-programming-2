class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        count = Counter()
        for t in time:
            res += count[-t % 60]
            count[t % 60] += 1
            
        return res