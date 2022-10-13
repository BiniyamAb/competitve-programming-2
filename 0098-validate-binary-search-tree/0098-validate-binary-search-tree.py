# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recur(root,smallest,biggest):
            if not root: return True
            if root.val <= smallest: return False
            else:  new_small = root.val
                
            if root.val >= biggest: return False
            else: new_big = root.val
            
            return recur(root.right,new_small,biggest) and recur(root.left,smallest,new_big)
        
        return recur(root,float("-inf"),float("inf"))
        # return recur(root.right,root.val,root.val) and recur(root.left,root.val,root.val)
            
        