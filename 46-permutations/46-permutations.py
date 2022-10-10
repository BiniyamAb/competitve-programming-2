class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        path_set = set()
        def dfs(i,path):
            num = nums[i]
            path.append(nums[i])
            path_set.add(nums[i])
            for j in range(len(nums)):
                if nums[j] not in path_set:
                    dfs(j,path)
            
            if len(path) == len(nums):
                res.append(path.copy())
            path.pop()
            path_set.remove(nums[i])
        
        for i in range(len(nums)):
            dfs(i, path)
        
        return res
            
            
        