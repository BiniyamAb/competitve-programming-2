class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, 1, [0]

        for char in s:
            
            if char ==' ': continue
            elif char.isdigit():
                num = (num * 10) + int(char)

            elif char == '+':
                stack[-1] += num * sign
                num = 0
                sign = 1

            elif char == '-':
                stack[-1] += num * sign
                num = 0
                sign = -1
                
            elif char == '(':
                stack.extend([sign,0])
                num = 0
                sign = 1
                
            elif char == ')':
                num_last = (stack.pop() + num*sign) * stack.pop()
                stack[-1] += num_last
                num = 0
                sign = 1
                
        return stack[-1] + num * sign