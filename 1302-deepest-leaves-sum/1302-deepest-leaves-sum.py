# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def find_depth(node):
            if not node: return 0
            return max(find_depth(node.left),find_depth(node.right))+1
        
        level = find_depth(root)
        self.sum = 0
        def dfs(node,lev):
            if not node.right and not node.left and lev == level:
                self.sum += node.val
                return
            if node.left: dfs(node.left,lev+1)
            if node.right: dfs(node.right,lev+1)
        
        dfs(root,1)
        return self.sum
        