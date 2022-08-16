class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def isPrefix(prefix,word):
            if len(word) < len(prefix): return False
            for i in range(len(prefix)):
                if word[i] != prefix[i]: return False
            return True
        
        count = 0
        for word in words:
            if isPrefix(pref,word): count+=1
        
        return count