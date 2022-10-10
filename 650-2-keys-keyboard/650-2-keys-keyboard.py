class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dfs(notepad,copied,n):
            if notepad > n:
                return float("inf")
            if notepad == n:
                return 0

            copy_paste = dfs(notepad*2,notepad,n) + 2
            paste = dfs(notepad+copied,copied,n) + 1

            return min(copy_paste,paste)
        
        if n == 1: return 0
        steps = dfs(2,1,n) + 2
        return steps