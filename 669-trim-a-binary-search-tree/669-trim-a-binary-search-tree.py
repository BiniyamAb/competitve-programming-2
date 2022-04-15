# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def dfs(head):
            if not head: return None
            if head.val < low: return dfs(head.right)
            if head.val > high: return dfs(head.left)
            
            head.left = dfs(head.left)
            head.right = dfs(head.right)
            return head
        
        return dfs(root)
            

                