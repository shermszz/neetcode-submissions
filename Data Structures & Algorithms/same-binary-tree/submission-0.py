# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

"""
=========================================================
KEY LEARNINGS: Same Tree (LeetCode 100)
=========================================================

CORE CONCEPTS:
1. Simultaneous Traversal: When comparing two trees, don't 
   linearize them into arrays (Inorder traversals cannot uniquely 
   define tree shapes anyway). Traverse them both at the same 
   time using recursive lockstep.
2. The 3 Checks:
   - Both None? True.
   - One None? False.
   - Values differ? False.
3. Time/Space: 
   - Time: O(min(N, M)) where N and M are the number of nodes. 
     (It stops early the second it finds a mismatch).
   - Space: O(min(H1, H2)) for the recursive call stack.

GUIDING HINTS:
- Keep the Python clean by checking `not p and not q` first, 
  followed immediately by `not p or not q`. 
- Be careful with Python syntax! If you break a `return` statement 
  across two lines, wrap the entire statement in `( )`.
=========================================================
"""

