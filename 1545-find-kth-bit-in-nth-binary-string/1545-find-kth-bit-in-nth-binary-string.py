class Solution:
    
    def helper(self, n):
        if n == 1:
            return "0"
        lower = self.helper(n-1)
        temp = [s for s in lower]
        for i in range(len(temp)): temp[i] = "0" if temp[i] == "1" else "1"
        temp.reverse()
        reverse = "".join(temp)
        
        return lower + "1" + reverse
        
    def findKthBit(self, n: int, k: int) -> str:
        str1 = self.helper(n)
        return str1[k-1]
        
            
        