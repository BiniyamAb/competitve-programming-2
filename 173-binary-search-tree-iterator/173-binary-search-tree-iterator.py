# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.list = []
        self.pointer = 0
        self.dfs(root)
        
    def dfs(self, node):
        if node:
            self.dfs(node.left)
            self.list.append(node.val)
            self.dfs(node.right)

    def next(self) -> int:
        self.pointer+=1
        return self.list[self.pointer-1]

    def hasNext(self) -> bool:
        return self.pointer < len(self.list)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()