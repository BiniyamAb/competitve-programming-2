class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs, visited, lst, path = [], set(), [], set()
        
        def dfs():
            if len(lst) == k:
                temp = list(lst)
                temp.sort()
                tup = tuple(temp)
                if tup not in visited and sum(lst) == n:
                    combs.append(temp)
                    visited.add(tup)
                return
            for i in range(1,10):
                if i not in path:
                    lst.append(i)
                    path.add(i)
                    dfs()
                    lst.pop()
                    path.remove(i)
        dfs()
        return combs
        
            