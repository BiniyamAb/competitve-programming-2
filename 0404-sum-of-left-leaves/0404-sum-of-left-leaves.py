# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node,is_left):
            if not node: return 0
            left = dfs(node.left,True)
            right = dfs(node.right,False)
            if is_left and (not node.left and not node.right):
                return node.val
            return left + right
        
        return dfs(root,False)