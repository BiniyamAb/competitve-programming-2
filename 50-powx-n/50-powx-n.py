class Solution:
    def myPow(self, x: float, n: int) -> float:      
        if n == 1: return x
        if n == 0: return 1

        if n < 0: x = 1/x
        half = self.myPow(x,abs(n)//2)
            
        return half*half if n%2==0 else half*half*x
            
        