# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Check if the current node is good or not
            res = 1 if node.val >= max_so_far else 0

            # Update maximum for the children
            max_so_far = max(node.val, max_so_far)

            # Return score + scores of the left and right branches
            return res + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
        
        return dfs(root, root.val)
        
"""
=========================================================
KEY LEARNINGS: Count Good Nodes in Binary Tree (LeetCode 1448)
=========================================================

CORE CONCEPTS:
1. Path-Specific State: When you need to track a value along a 
   specific path from root-to-leaf (like a high score), pass it 
   DOWN as a parameter in your recursive function. 
2. Pure vs. Impure Recursion:
   - Impure: Using `nonlocal count` and updating it as a side-effect.
   - Pure: `return my_score + dfs(left) + dfs(right)`.

GUIDING HINTS:
- Keep the state isolated! Reassign `max_so_far` inside the function 
  call so it doesn't "leak" across branches:
  `dfs(node.left, max(max_so_far, node.val))`
- Base case: `if not node: return 0`
- The Root Kickoff: `dfs(root, root.val)` ensures the root is 
  judged against itself (meaning it is always a Good Node).
=========================================================
"""