class Solution:
    def toList(self, s):
        arr = []
        for i in range(len(s)):
            if s[i] != "#": arr.append(s[i])
            elif arr: arr.pop()
        return arr            
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = self.toList(s)
        new_t = self.toList(t)
        
        return "".join(new_s) == "".join(new_t)
        