class Solution:
    
    def longestStrChain(self, words: List[str]) -> int:
        path = set()
        
        def isPredecessor(word1, word2):
            if len(word2) - len(word1) != 1: 
                return False
            
            pointer1 = pointer2 = 0
            removal_used = False
            
            while pointer1 < len(word1) and pointer2 < len(word2):
                if word1[pointer1] != word2[pointer2] and not removal_used:
                    pointer1 -= 1
                    removal_used = True
                    
                elif word1[pointer1] != word2[pointer2]:
                    return False
                
                pointer1 += 1
                pointer2 += 1
            
            return True
        
        @cache
        def dp(i):
            max_length = 0
            path.add(i)
            for j in range(len(words)):
                if j != i and j not in path and isPredecessor(words[i], words[j]):
                    length = dp(j)
                    max_length = max(max_length, length)
                    
            path.remove(i)
            return max_length + 1
        
        max_length = 1
        for i in range(len(words)):
            length = dp(i)
            max_length = max(max_length, length)
        
        return max_length
                    
            
                