class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        if len(prices) == 1: return 1
        num_of_subarrays = lambda n: (n * (n+1)/2) - n
        l = count = 0
        for r in range(1,len(prices)):
            if prices[r-1] - prices[r] != 1:
                count += num_of_subarrays(r-l)
                l = r   

        count += num_of_subarrays(r-l+1)
        count += len(prices)
        
        return int(count)
        