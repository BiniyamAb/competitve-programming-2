# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictionary = defaultdict(list)
        queue = deque([(root, 0, 0)])
        ans = []
        while queue:
            for _ in range(len(queue)):
                node, horizontal, vertical = queue.popleft()
                dictionary[horizontal].append((vertical,node.val))
                if node.left:
                    queue.append((node.left, horizontal-1, vertical-1))
                if node.right:
                    queue.append((node.right, horizontal+1, vertical-1))
                    
        for i in sorted(dictionary.keys()):
            curr_level = [x[1] for x in sorted(dictionary[i],key=lambda x:(-x[0],x[1]))]
            ans.append(curr_level)
        
        return ans
        