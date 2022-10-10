class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(i,path):
            num = nums[i]
            path.append(nums[i])
            for j in range(len(nums)):
                if nums[j] not in path:
                    dfs(j,path)
            
            if len(path) == len(nums):
                res.append(path.copy())
            path.pop()
        
        for i in range(len(nums)):
            dfs(i, path)
        
        return res
            
            
        