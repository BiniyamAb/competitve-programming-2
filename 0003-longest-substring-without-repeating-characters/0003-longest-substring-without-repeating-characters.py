class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l = longest = 0
        for r in range(len(s)):
            if s[r] not in visited:
                visited.add(s[r])
                continue
            longest = max(longest, r-l)
            while s[l] != s[r] and l < r:
                visited.remove(s[l])
                l+=1
            l+=1
        return max(longest, len(s)-l)