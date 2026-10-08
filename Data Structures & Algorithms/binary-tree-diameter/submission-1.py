# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
          GOAL: Return the maximum distance between any two nodes inside the tree.
          The distance between any 2 nodes must be the longest one

          We can use a similar idea to finding the maximum depth of the tree.
          The only difference is that the maximum depth starts from the root. For this question, we can start from any node to any other node.

          We need to keep track of 2 different things
            1. The actual diamater of the tree 
            2. The height of the tree

        """
        res = 0 # This is to track the actual diameter of the tree

        def dfs(curr_node):
          # This function returns the HEIGHT of the binary tree that we are at 
          if not curr_node:
            return 0
          
          left = dfs(curr_node.left)
          right = dfs(curr_node.right)

          nonlocal res
          res = max(res, left + right)

          return 1 + max(left, right)
        dfs(root)
        return res



