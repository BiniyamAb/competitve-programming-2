# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.dp(root,True)
    
    @cache
    def dp(self,node,canPick):
        if not node: return 0
        pick = 0
        if canPick:
            pick_to_right = self.dp(node.right,False)
            pick_to_left = self.dp(node.left,False)
            pick = pick_to_right + pick_to_left + node.val
            
        not_pick_to_right = self.dp(node.right,True)
        not_pick_to_left = self.dp(node.left,True)
        not_pick = not_pick_to_right + not_pick_to_left
        
        return max(pick,not_pick)