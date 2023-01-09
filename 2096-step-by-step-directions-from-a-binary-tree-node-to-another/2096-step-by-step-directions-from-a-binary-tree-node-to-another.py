# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent = {}
        startNode = None
        def traverse(node):
            nonlocal startNode
            if node.val == startValue:
                startNode = node
            if node.left:
                parent[node.left] = node
                traverse(node.left)
            if node.right:
                parent[node.right] = node
                traverse(node.right)
            
        traverse(root)

        visited = set()
        res = []
        path = []
        def findPath(node):
            nonlocal res
            visited.add(node.val)
            if node.val == destValue:
                res = path.copy()
                return
            
            if node.left and node.left.val not in visited:
                path.append("L")
                findPath(node.left)
                path.pop()
            if node.right and node.right.val not in visited:
                path.append("R")
                findPath(node.right)
                path.pop()
            if node in parent and parent[node].val not in visited:
                path.append("U")
                findPath(parent[node])
                path.pop()
        
        findPath(startNode)
        return "".join(res)
        
        
        
        
        
                
            