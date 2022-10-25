class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        LPS = [0] * len(needle)
        pointer = 0
        for i in range(1,len(needle)):
            while pointer != 0 and needle[i] != needle[pointer]:
                pointer = LPS[pointer-1]
            
            if needle[pointer] == needle[i]:
                LPS[i] = pointer + 1
                pointer += 1
        pointer = 0
        for i in range(len(haystack)):
            while pointer != 0 and haystack[i] != needle[pointer]:
                pointer = LPS[pointer-1]
            
            if needle[pointer] == haystack[i]:
                pointer += 1
            
            if pointer == len(needle):
                return i - len(needle) + 1
        
        return -1
            
            