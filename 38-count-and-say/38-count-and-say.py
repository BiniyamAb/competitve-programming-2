class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            num = s[0]
            new_s = ""
            count = 1
            for i in range(1,len(s)):
                if s[i] != num:
                    new_s += str(count) + str(num)
                    num = s[i]
                    count = 1
                else: count += 1
            
            new_s += str(count) + str(num)
            s = new_s
        
        return s
            