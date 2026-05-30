# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative approach (in case of extremely inbalanced tree) --> Use BFS
        if not root:
            return 0
        queue, maximum = deque(), 0
        queue.append((root, 1)) # Root if it exists is at depth 1
        while queue:
            node, depth = queue.popleft()
            maximum = max(maximum, depth)
            if node.left:
                queue.append((node.left, 1 + depth))
            if node.right:
                queue.append((node.right, 1 + depth))
        return maximum


"""
=========================================================
KEY LEARNINGS: Maximum Depth of Binary Tree (LeetCode 104)
=========================================================

CORE CONCEPTS:
1. Recursive DFS (Top-Down): Cleanest code. `1 + max(left, right)`. 
   Can cause Stack Overflow on extremely skewed trees.
2. Iterative BFS (Level Order): Uses a `collections.deque`. Best 
   for finding shortest paths or processing level-by-level.
3. Iterative DFS (Pre-Order): Uses a standard Python list as a `stack`. 
   Mimics the recursive call stack safely in heap memory.

GUIDING HINTS:
- The Tuple Method: Storing `(node, current_depth)` in your stack/queue 
  is a foolproof way to track state without global variables.
- The Batch BFS Method: `for _ in range(len(queue)):` allows you to 
  process a tree exactly one horizontal level at a time.
- The Stack vs Queue Trick: `popleft()` makes it BFS. `pop()` makes 
  it Iterative DFS. The underlying while-loop structure is identical!
=========================================================
"""