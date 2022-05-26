class Solution:
    def reverseBits(self, n: int) -> int:
        new = 0
        for _ in range(32):
            new <<= 1
            if n & 1: new+=1
            n >>= 1
        
        return new
            
        