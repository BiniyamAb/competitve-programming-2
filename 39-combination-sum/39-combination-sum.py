class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i,sum,path):
            sum += candidates[i]
            path.append(candidates[i])
            if sum < target:
                for j in range(i,len(candidates)):
                    dfs(j,sum,path)
            elif sum == target:
                res.append(path.copy())
            
            path.pop()
        
        for i in range(len(candidates)):
            dfs(i,0,path)
        
        return res