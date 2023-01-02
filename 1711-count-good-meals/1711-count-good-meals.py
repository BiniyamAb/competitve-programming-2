class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 1000000007
        lookup = defaultdict(int)
        count = 0
        for i, amount in enumerate(deliciousness):
            count = (count % mod) + lookup[amount] % mod
            for p in range(0,22):
                diff = (2**p) - amount
                lookup[diff] += 1
        
        return count
                
        