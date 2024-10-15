class Solution:
    def minimumSteps(self, s: str) -> int:
        black_ind = self.getFirstBlackIndex(s)
        if black_ind == -1: return 0
        
        swaps = 0
        for i in range(black_ind+1, len(s)):
            if s[i] == "0":
                swaps += (i - black_ind)
                black_ind += 1
        
        return swaps       
    
    def getFirstBlackIndex(self,s):
        for ind, color in enumerate(s):
            if color == "1": return ind
        
        return -1