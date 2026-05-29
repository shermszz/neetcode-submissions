# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            # If no root, or root is the only TreeNode, then return it
            return root
        left = root.left 
        right = root.right
        root.left = self.invertTree(right)
        root.right = self.invertTree(left)
        return root