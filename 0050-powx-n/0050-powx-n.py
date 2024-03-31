class Solution:
    def myPow(self, x: float, n: int) -> float:      
        if n == 1: return x
        if n == 0: return 1

        if n < 0: x = 1/x
        halfPower = self.myPow(x,abs(n)//2)
            
        return halfPower*halfPower if n%2==0 else halfPower*halfPower*x
            