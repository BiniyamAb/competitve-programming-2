class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        adj = [1]
        stack = [s[0]]
        for i in range(1,len(s)):
            if stack and s[i] == stack[-1]:
                adj[-1]+=1
            else:
                adj.append(1)
            stack.append(s[i])
            if adj[-1] == k:
                for _ in range(k): stack.pop()
                adj.pop()
                
        return "".join(stack)