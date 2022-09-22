class Solution:
    def reverseWords(self, s: str) -> str:
        to_reverse = []
        res = []
        for st in s:
            if st != " ":
                to_reverse.append(st)
                continue
            while to_reverse:
                res.append(to_reverse.pop())
            res.append(" ")
            
        while to_reverse:
            res.append(to_reverse.pop())
        return "".join(res)
        
        
        