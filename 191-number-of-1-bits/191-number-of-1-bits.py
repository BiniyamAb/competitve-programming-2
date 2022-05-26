class Solution:
    def hammingWeight(self, n: int) -> int:
        s = bin(n)[2:]
        return s.count("1")
        