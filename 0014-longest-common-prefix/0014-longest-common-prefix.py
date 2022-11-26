class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minn_length = len(strs[0])
        for st in strs:
            minn_length = min(minn_length, len(st))
        
        prefix = []
        for i in range(minn_length):
            not_same = False
            char = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != char:
                    not_same = True
                    break
            if not not_same:
                prefix.append(char)
            else: break
        
        return "".join(prefix)
                
        
        