class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = "".join(set(s))
        length = 1
        for letter in letters:
            start = 0
            temp_k = k
            for i in range(len(s)):
                if s[i] == letter:
                    pass
                elif temp_k > 0:
                    temp_k-=1
                else:
                    length = max(length, i-start)
                    while temp_k == 0 and start <= i:
                        if s[start] != letter: temp_k+=1
                        start+=1
                    temp_k = 0
            length = max(length, i-start+1)
        
        return length
        
        
        