class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_open = []
        stack_stars = []
        
        for i in range(len(s)):
            if s[i] == "(":
                stack_open.append(i)
            elif s[i] == "*":
                stack_stars.append(i)
            else:
                if stack_open:
                    stack_open.pop()
                elif stack_stars:
                    stack_stars.pop()
                else:
                    return False
        while stack_open:
            if stack_stars:
                if stack_open.pop() > stack_stars.pop():
                    return False
            else:
                return False
        return True