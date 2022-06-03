class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        four = n//2
        five = n-four
        
        return ((pow(5,five,mod)) * (pow(4,four,mod))) % mod
        