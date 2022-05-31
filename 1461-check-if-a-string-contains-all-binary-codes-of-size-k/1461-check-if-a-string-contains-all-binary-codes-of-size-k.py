class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = 2**k
        subs = set()
        for i in range(len(s)-k+1):
            subs.add(s[i:i+k])
            if len(subs) == n: return True
        
        return False
        