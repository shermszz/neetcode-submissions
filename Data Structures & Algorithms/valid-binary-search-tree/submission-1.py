# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_dfs(node, lower, upper):
            if not node:
                return True
            
            if not (lower < node.val < upper):
                return False
            
            return inorder_dfs(node.left, lower, node.val) and inorder_dfs(node.right, node.val, upper)
        return inorder_dfs(root, -float('inf'), float('inf'))

"""
=========================================================
KEY LEARNINGS: Validate Binary Search Tree (LeetCode 98)
=========================================================

CORE CONCEPTS:
1. Top-Down Bounds: A node isn't just compared to its parent; 
   it is constrained by EVERY ancestor above it. Pass `lower` 
   and `upper` bounds down the recursive calls.
2. Short-Circuiting: Use `return dfs(left) and dfs(right)` to 
   instantly kill the traversal the moment a `False` is found, 
   preventing you from wasting time on the rest of the tree.

GUIDING HINTS:
- Left Child updates the UPPER bound: `dfs(node.left, lower, node.val)`
- Right Child updates the LOWER bound: `dfs(node.right, node.val, upper)`
- Python handles infinity with `float('inf')` and `float('-inf')`.
=========================================================
"""


