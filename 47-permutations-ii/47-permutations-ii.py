class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, path, lst, combs = [], set(), [], set()
        
        def dfs():            
            for i in range(len(nums)):
                if i not in path:
                    path.add(i)
                    lst.append(nums[i])
                    
                    if len(lst) == len(nums):
                        tup = tuple(lst)
                        if tup not in combs:
                            res.append(list(lst))
                            combs.add(tup)
                    else:dfs()
                        
                    lst.pop()
                    path.remove(i)
        
        dfs()
        return res
        