class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:        
        
        def calculate(op, x, y):
            if op == "-": return x - y
            if op == "+": return x + y
            if op == "*": return x * y
        
        @cache
        def backtrack(left, right):
            result = []
            for i in range(left, right):
                if expression[i] in "+-*":
                    for x in backtrack(left, i):
                        for y in backtrack(i + 1, right):
                            result.append(calculate(expression[i], x, y))

            if not result: result = [int(expression[left:right])]
            return result
        
        ans = backtrack(0, len(expression))
        return ans