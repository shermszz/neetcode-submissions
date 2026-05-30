# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Run DFS from the root node, visiting left then right 
        if not root:
            return 0
        maximum = max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        return maximum
