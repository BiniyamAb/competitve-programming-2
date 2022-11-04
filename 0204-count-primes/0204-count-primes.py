class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        isPrime = [True for i in range(n)]
        isPrime[0] = isPrime[1] = False
        i = 2
        while i * i < n:
            if isPrime[i]:
                j = i * i
                for j in range(i*i,n,i):
                    isPrime[j] = False
            i += 1
        
        return isPrime.count(True)
