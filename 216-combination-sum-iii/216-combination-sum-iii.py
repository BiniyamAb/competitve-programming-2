class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, visited, lst, combs = [], set(), [], set()
        def dfs(sum, num):
            visited.add(num)
            lst.append(num)
            sum+=num
            if len(lst) == k:
                if sum == n: 
                    temp_lst = list(lst)
                    temp_lst.sort()
                    tup = tuple(temp_lst)
                    if tup not in combs:
                        res.append(list(lst))   
                        combs.add(tup)
                lst.pop()
                visited.remove(num)
                return
                
            for i in range(1,10):
                if i not in visited:
                    dfs(sum, i)
                    
            lst.pop()
            visited.remove(num)
            
        for i in range(1,10):
            dfs(0, i)
        
        return res
            
        