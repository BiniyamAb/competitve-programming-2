class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combs = {'2':"abc", '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        def dfs(i, order):
            button = combs[digits[i]]
            next_ = i+1 < len(digits)
            for l in button:
                order.append(l)
                if next_:
                    dfs(i+1,order)
                else:
                    res.append("".join(order))
                order.pop()
                
        if digits: dfs(0,[])
        return res
        