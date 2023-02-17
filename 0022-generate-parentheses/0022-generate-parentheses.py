class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def bt(openn, closed, path):
            nonlocal n
            if openn + closed == n * 2:
                res.append("".join(path))
                return
            
            if openn < n:
                path.append("(")
                bt(openn + 1, closed, path)
                path.pop()
            
            if closed < openn:
                path.append(")")
                bt(openn, closed + 1, path)
                path.pop()
        
        bt(0,0,path)
        return res
        