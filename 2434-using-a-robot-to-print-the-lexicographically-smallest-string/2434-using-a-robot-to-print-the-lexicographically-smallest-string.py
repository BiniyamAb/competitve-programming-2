class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)
        t = []
        p = []
        for i in range(len(s)):
            char = s[i]
            t.append(char)
            freq[char] -= 1
            while t and not self.lowerExist(s,freq,t[-1]):
                p.append(t.pop())
        
        return "".join(p)         
    
    
    def lowerExist(self,s,freq,char):
        ordd = ord(char)
        for k,v in freq.items():
            if ord(k) < ordd and v > 0:
                return True
            
        return False
            