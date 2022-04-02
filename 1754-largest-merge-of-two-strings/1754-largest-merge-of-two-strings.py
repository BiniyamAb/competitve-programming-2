class Solution:
    def Larger(self, i1, i2, word1, word2):
        while i1 < self.len1 and i2 < self.len2:
            if word1[i1] > word2[i2]:
                return 1
            elif word2[i2] > word1[i1]:
                return 2
            i1+=1
            i2+=1
        
        if i1 < self.len1: return 1
        if i2 < self.len2: return 2
        
        return 1   
        
    def largestMerge(self, word1: str, word2: str) -> str:
        self.len1, self.len2 = len(word1), len(word2)
        merged = []
        i1 = i2 = 0
        
        while i1 < self.len1 or i2 < self.len2:
            if not i1 < self.len1:
                merged.append(word2[i2])
                i2+=1
            elif not i2 < self.len2:
                merged.append(word1[i1])
                i1+=1
            else:
                toMerge = self.Larger(i1, i2, word1, word2)
                if toMerge == 1:
                    merged.append(word1[i1])
                    i1+=1
                else:
                    merged.append(word2[i2])
                    i2+=1
        
        return "".join(merged)
        
        