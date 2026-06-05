# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = [] # To record the overall list of lists
        while queue:
            level = [] # A new list for every level
            for _ in range(len(queue)):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right: 
                    queue.append(curr.right)
            res.append(level) # Append the number of nodes for that level
        return res

"""
=========================================================
KEY LEARNINGS: Binary Tree Level Order Traversal (LeetCode 102)
=========================================================

CORE CONCEPTS:
1. Breadth-First Search (BFS): The absolute best algorithm for 
   anything requiring a "level-by-level" or "shortest path" traversal.
2. The Level Snapshot: Because BFS queues grow dynamically, you 
   must freeze the current level's size before popping.

GUIDING HINTS:
- Use `collections.deque` for O(1) pops from the front. Standard 
  Python lists take O(N) time to `pop(0)`.
- The BFS Skeleton:
  1. `queue = deque([root])`
  2. `while queue:`
  3. `level_length = len(queue)`
  4. `for _ in range(level_length):`
  5. `node = queue.popleft()`
  6. Append children to queue.
- Time: O(N)
- Space: O(N) (The bottom level of a balanced tree holds N/2 nodes).
=========================================================
"""