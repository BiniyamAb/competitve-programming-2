# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if not node: return [float("-inf"),0]
        
        left_max, left_extensible = self.dfs(node.left)
        right_max, right_extensible = self.dfs(node.right)
        
        current_max = left_extensible + right_extensible + node.val
        one_way_max = max(left_extensible, right_extensible, 0) + node.val
        max_of_all = max(left_max, right_max, current_max, one_way_max)
        
        return [max_of_all, one_way_max]
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = self.dfs(root)
        return max(result)
        
        
        
        