class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        s1 = Counter(words1)
        s2 = Counter(words2)
        count = 0
        for s in words1:
            if s in words2 and s1[s] == 1 and s2[s] == 1: count +=1
        
        return count