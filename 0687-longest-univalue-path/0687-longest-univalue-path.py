# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:        
        if not root: return 0
        def dfs(node):
            path = [1, 1]
            one = 0
            if node.right:
                diff, same = dfs(node.right)
                if node.val == node.right.val:
                    path[1] += same
                    one = max(one, same)
                path[0] = max(path[0], diff)
                
            if node.left:
                diff, same = dfs(node.left)
                if node.val == node.left.val:
                    path[1] += same
                    one = max(one, same)
                path[0] = max(path[0], diff)
            
            path[0] = max(path)
            path[1] = one + 1
            return path
        
        
        path = dfs(root)
        return max(path) - 1