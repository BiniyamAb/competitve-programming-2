class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = [0] * len(s)
        a = [0] * len(s)
        
        b_count = 0
        a_count = 0
        for i in range(len(s)):
            b[i] = b_count
            if s[i] == "b":
                b_count += 1
                
            a[-i-1] = a_count
            if s[-i-1] == "a":
                a_count += 1
        
        
        minn = len(s)
        for i in range(len(s)):
            minn = min(minn, a[i] + b[i])
        
        return minn
        
            