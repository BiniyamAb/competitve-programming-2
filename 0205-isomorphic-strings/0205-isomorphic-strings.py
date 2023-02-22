class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_mapp = {}
        t_mapp = {}
        for i in range(len(s)):
            if s[i] in s_mapp and s_mapp[s[i]] != t[i]: return False
            if t[i] in t_mapp and t_mapp[t[i]] != s[i]: return False
            s_mapp[s[i]] = t[i]
            t_mapp[t[i]] = s[i]
        
        return True
        