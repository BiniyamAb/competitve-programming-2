"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return None
        queue, res = deque([root]), []
        while queue:
            lst = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                for node in curr.children:
                    queue.append(node)
                lst.append(curr.val)
            res.append(lst)
        
        return res
                
        