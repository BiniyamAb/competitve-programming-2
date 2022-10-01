class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort(reverse=True)
        g.sort(reverse=True)
        length_of_s = len(s)
        s_pointer = count = 0
        for i in range(len(g)):
            if s_pointer < length_of_s and s[s_pointer] >= g[i]:
                s_pointer += 1
                count += 1
        
        return count