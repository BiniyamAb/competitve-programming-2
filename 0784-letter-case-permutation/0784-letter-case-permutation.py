class Solution:
    def bt(self,i,s,path,possible):
        path.append(s[i])
        if len(path) == len(s):
            possible.append("".join(path))
            if not s[i].isdigit():
                path[-1] = s[i].swapcase()
                possible.append("".join(path))                
        else:
            self.bt(i+1,s,path,possible)
            if not s[i].isdigit():
                path[-1] = s[i].swapcase()
                self.bt(i+1,s,path,possible)
        path.pop()
    
    def letterCasePermutation(self, s: str) -> List[str]:
        possible = []
        self.bt(0,s,[],possible)
        
        return possible
        
        