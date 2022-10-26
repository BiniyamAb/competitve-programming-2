class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= len(part) and stack[-1] == part[-1]: 
                if self.hasMatch(stack,part):
                    for _ in range(len(part)):
                        stack.pop()

        return "".join(stack)
    
    def hasMatch(self,stack,part):
        pointer = len(stack) - 1
        for i in range(len(part)-1,-1,-1):
            if part[i] != stack[pointer]:
                return False
            pointer -= 1
        return True
