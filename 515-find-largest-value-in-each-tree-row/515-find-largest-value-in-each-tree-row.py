# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        queue, res = deque([root]), []
        while queue:
            maxx = float("-inf")
            for i in range(len(queue)):
                curr = queue.popleft()
                maxx = max(maxx, curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            
            res.append(maxx)
        
        return res
        