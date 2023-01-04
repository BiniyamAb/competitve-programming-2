class Solution:
    def firstUniqChar(self, s: str) -> int:
        indices = defaultdict(list)
        for i in range(len(s)):
            indices[s[i]].append(i)
        
        index = float("inf")
        for k, v in indices.items():
            if len(v) == 1:
                index = min(index, v[0])
        
        if index == float("inf"): return -1
        return index
        