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
            head.left = dfs(head.left)
            head.right = dfs(head.right)
            
            if head.val < low: return head.right
            elif head.val > high: return head.left
            else: return head
            
        return dfs(root)
            

                