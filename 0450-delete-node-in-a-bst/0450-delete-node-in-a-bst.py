# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return root
        node, parent, right = root, None, False
        while root:
            if root.val == key: break  
            if root.val > key: parent, root, right = root, root.left, False
            else: parent, root, right = root, root.right, True
        if not root: return node
        if (not root.right and not root.left) and not parent and root.val == key: return
        if not root.right or not root.left:
            if root.right and not root.left: chosen = root.right
            elif root.left and not root.right: chosen = root.left
            elif not root.left and not root.right: chosen = None
            if not parent: return chosen
            if right: parent.right = chosen
            else: parent.left = chosen
            return node
        else:
            leftChild = root.left
            rightChild = root.right
            while rightChild.left: rightChild = rightChild.left
            rightChild.left = leftChild
            if root == node: return root.right
            else:
                chosen = root.right
                if right: parent.right = chosen
                else: parent.left = chosen
                return node