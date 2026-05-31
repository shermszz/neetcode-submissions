# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDiameter = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
      if not root:
        return 0
      
      def dfs(node):
        if not node:
          return 0
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        # Calculate the local diameter by adding up left and right depths to see if it exceeds current max
        self.maxDiameter = max(self.maxDiameter, left_depth + right_depth) 

        return 1 + max(left_depth, right_depth) # return this node's depth to the parent
      
      dfs(root) # Start dfs on the root
      return self.maxDiameter

"""
=========================================================
KEY LEARNINGS: Diameter of Binary Tree (LeetCode 543)
=========================================================

CORE CONCEPTS:
1. Depth vs. Diameter: Depth is the longest path down to ONE leaf. 
   Diameter is the longest path between ANY TWO nodes 
   (Local Diameter = Left Depth + Right Depth).
2. The "Two Jobs" Problem: The DFS function must calculate the 
   Diameter for the final answer, but it MUST return the Depth 
   so parent nodes can do their own math.
3. The Nested Helper Pattern: The cleanest way to manage state in 
   Python tree problems is a `dfs()` helper nested inside the main 
   function, modifying a `self.result` variable.

GUIDING HINTS:
- The Skeleton:
  1. `self.max_diam = 0`
  2. `def dfs(node):`
  3. `if not node: return 0`
  4. `left, right = dfs(node.left), dfs(node.right)`
  5. `self.max_diam = max(self.max_diam, left + right)  <-- Side Quest!`
  6. `return 1 + max(left, right)                       <-- Main Job!`
  7. Kickoff: `dfs(root)`
  8. `return self.max_diam`
=========================================================
"""
