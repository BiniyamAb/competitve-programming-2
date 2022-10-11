# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node,prev):
            if not node: return prev
            right = dfs(node.right, prev)
            left = dfs(node.left,right+node.val)
            node.val = right + node.val
            
            return left
        
        dfs(root,0)
        
        return root