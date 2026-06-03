# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
          return True 

        diff = 0

        def dfs(node):
          if not node:
            return 0
          
          left_depth = dfs(node.left) # Get the left depth
          right_depth = dfs(node.right) # Get the right depth

          if left_depth == -1 or right_depth == -1:
            return -1

          diff = abs(left_depth - right_depth)

          if diff > 1:
            return -1
          
          return 1 + max(left_depth, right_depth)
        
        return dfs(root) != -1

"""
=========================================================
KEY LEARNINGS: Balanced Binary Tree (LeetCode 110)
=========================================================

CORE CONCEPTS:
1. The Bottom-Up Poison Pill: To check if EVERY node is balanced 
   in O(N) time, you must process from the bottom up. If any subtree 
   is unbalanced, return a "poisoned" fake height (like -1) to 
   instantly fail the entire tree.
2. Perspective Trap: A recursive function doesn't know if it was 
   called as a left or right child. Its only job is to calculate the 
   height of the tree rooted AT ITSELF: `1 + max(left, right)`.

GUIDING HINTS:
- Structure your `dfs(node)` helper with 3 checks:
  1. Did a child return -1? -> return -1
  2. Is `abs(left - right) > 1`? -> return -1
  3. Otherwise, return true height -> `1 + max(left, right)`
- Main function kickoff: `return dfs(root) != -1`
- Why O(N)? Because we compute the height and balance at the exact 
  same time. If you use two separate functions (a balance checker 
  that calls a height checker), you traverse the same nodes repeatedly, 
  ruining time complexity to O(N^2).
=========================================================
"""

        


