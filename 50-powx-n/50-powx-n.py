class Solution:
    def myPow(self, x: float, n: int) -> float:       
        if n < 0: 
            x = 1 / x
        answer = self.helper(x,abs(n))
        return answer

    def helper(self,x,n):
        if n == 0: return 1
        if n == 1: return x

        half = self.helper(x,n//2)
        answer = half * half

        if n%2 != 0: 
            answer = answer * x
        
        return answer
            
        