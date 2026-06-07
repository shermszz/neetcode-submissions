# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Recursive solution using inorder and a global counter

        found, count, res = False, 0, 0
        def inorder(node, k):
            nonlocal found
            nonlocal res
            nonlocal count

            if not node:
                return
            
            if found: # Once we have found the value, stop traversing 
                return

            inorder(node.left, k)

            count += 1
            if count == k: 
                # Found the node that we are looking for
                found = True
                res = node.val
            
            inorder(node.right, k)
        inorder(root, k)
        return res

"""
=========================================================
KEY LEARNINGS: Kth Smallest Element in a BST (LeetCode 230)
=========================================================

CORE CONCEPTS:
1. BST Property: An In-Order Traversal (Left, Root, Right) of a 
   Binary Search Tree will ALWAYS visit the nodes in perfectly 
   sorted, ascending order.
2. Optimization: Never store the entire tree in an array if you 
   only need one specific element. Just keep a running count of 
   how many nodes you have "visited" and stop when count == k.

GUIDING HINTS:
- Recursive Approach: Use `nonlocal count` and `nonlocal res`. Add 
  an early return `if count >= k` to prevent unnecessary traversal.
- Iterative Approach (Recommended): Use a `while` loop and a `stack`.
  Dive left -> Pop & Process -> Go right. The `count` variable lives 
  locally, and you can just `return` directly from the loop!
- Time: O(H + k) where H is the height of the tree.
- Space: O(H) to hold the recursion/stack path down to the bottom.
=========================================================
"""
        