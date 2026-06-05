# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            # This means the LCA is on the right hand side
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val and q.val < root.val:
            # This means the LCA is on the left hand side
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Otherwise, if there is a disagreemnet, we are already at the LCA node
        return root

"""
=========================================================
KEY LEARNINGS: Lowest Common Ancestor of a BST (LeetCode 235)
=========================================================

CORE CONCEPTS:
1. The Split Point: In a BST, the LCA is simply the first node 
   you encounter where `p` and `q` disagree on which direction 
   to go. 
2. Tail Recursion: Because we don't need to combine answers from 
   the left and right (like we did in Max Depth), we can easily 
   convert the recursive solution into an iterative `while` loop.

GUIDING HINTS:
- Both targets > Root? -> Go Right.
- Both targets < Root? -> Go Left.
- Else (one is greater, one is less, or one IS the root) -> Return Root!
- Time Complexity: O(H) where H is the height of the tree.
- Space Complexity: O(1) if Iterative, O(H) if Recursive.
=========================================================
"""