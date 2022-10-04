class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False 
        s_dict, t_dict = Counter(s), Counter(t)
        for k,v in s_dict.items():
            if k not in t_dict or v != t_dict[k]:
                return False
        
        return True
        