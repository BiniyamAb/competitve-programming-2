class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic, taken = {}, set()
        words = s.split(" ")
        if len(pattern) != len(words): return False
        
        for i in range(len(pattern)):
            if dic.get(pattern[i]) is None:
                if words[i] in taken: return False
                dic[pattern[i]] = words[i]
                taken.add(words[i])
            elif dic[pattern[i]] != words[i]:
                return False
        
        return True
            
        