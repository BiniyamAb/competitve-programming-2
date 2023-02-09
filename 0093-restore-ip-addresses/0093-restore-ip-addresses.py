class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def bt(s, dots, path):
            if not dots:
                if len(s) >=2 and s[0] == '0':
                    return 
                if (s and int(s) <= 255):
                    res.append("".join([s]+path))
                return 
            
            if not dots or not s: return 
                     
            bt(s[:-1], dots-1, [".", s[-1]]+path)
            
            if len(s) >= 2 and s[-2] != "0":
                bt(s[:-2], dots-1, [".", s[-2:]]+path)
           
            if len(s) >= 3 and (s[-3] == "1" or (s[-3]=="2" and int(s[-3:]) <= 255)):
                bt(s[:-3], dots -1, [".", s[-3:]]+path)
          
        bt(s, 3, [])
        return res