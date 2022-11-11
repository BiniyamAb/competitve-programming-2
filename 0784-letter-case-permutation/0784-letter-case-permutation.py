class Solution:
    def bt(self,i,s,path,possible):
        path.append(s[i])
        if len(path) == len(s):
            possible.append("".join(path))
            if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
                path.pop()
                path.append(s[i].swapcase())
                possible.append("".join(path))                
        else:
            self.bt(i+1,s,path,possible)
            if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
                path.pop()
                path.append(s[i].swapcase())
                self.bt(i+1,s,path,possible)

        path.pop()
    
    
    def letterCasePermutation(self, s: str) -> List[str]:
        possible = []
        self.bt(0,s,[],possible)
        
        return possible
        
        