# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maximum = max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))
        return maximum

"""
=========================================================
KEY LEARNINGS: Maximum Depth of Binary Tree (LeetCode 104)
=========================================================

CORE CONCEPTS:
1. Bottom-Up DFS (Recursion): The depth of a tree is simply 
   1 (the root) + the maximum depth of its left or right subtrees.
2. Time Complexity: O(N) because we visit every single node.
3. Space Complexity: O(H) where H is the height of the tree. 
   In the worst case (a perfectly unbalanced tree/linked list), 
   space is O(N). In a perfectly balanced tree, it is O(log N).

GUIDING HINTS:
- Recursive Approach: `return 1 + max(dfs(left), dfs(right))`
- The "Stack Overflow" Trap: If an interviewer mentions massive 
  unbalanced trees, they want an Iterative solution.
- BFS Alternative: Use a Queue to process the tree level by level. 
  Every time you pop all the nodes currently in the queue 
  (finishing a level), increment a `level_count` by 1. 
- Iterative DFS Alternative: Use a Stack containing tuples of 
  `(node, current_depth)`. Every time you pop, update your 
  `max_depth` variable, and push children with `current_depth + 1`.
=========================================================
"""