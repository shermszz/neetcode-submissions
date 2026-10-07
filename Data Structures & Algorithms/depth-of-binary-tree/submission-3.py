# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
            GOAL: We want to find what is the maximum depth
            We count the root layer as depth = 1

            Base case: If root is null, then we return 0

            Otherwise, we are looking at one node and we know the deepest could lie on either the right or the left
            So from here, we need to track the max depth as we dive into the left and the right
        """

        # 1. Base case first
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

