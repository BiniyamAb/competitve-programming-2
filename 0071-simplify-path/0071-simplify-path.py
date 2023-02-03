class Solution:
    def simplifyPath(self, path: str) -> str:
        path += "/"
        stack = []
        temp = ""

        for char in path:
            if char != "/":
                temp += char
                
            else:
                if temp == "..":
                    if stack: stack.pop()
                elif temp != "" and temp != ".":
                    stack.append(temp)
                temp = ""
                
        return "/" + "/".join(stack)
        