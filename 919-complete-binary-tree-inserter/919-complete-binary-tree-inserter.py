# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.head = root
        self.queue = deque([root])
        self.adjust_level()
     
    def adjust_level(self):
        while self.queue:
            curr = self.queue[0]
            if curr.left and curr.right:
                self.queue.append(curr.left)
                self.queue.append(curr.right)
                self.queue.popleft()
            else: break

    def insert(self, val: int) -> int:
        node = TreeNode(val=val)
        parent_node = self.queue[0]
        if not parent_node.left: parent_node.left =  node
        else: parent_node.right = node
        self.adjust_level()
        return parent_node.val

    def get_root(self) -> Optional[TreeNode]:
        return self.head
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()