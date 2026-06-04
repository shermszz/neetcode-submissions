# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        if root is None and subRoot is None: # If both root == subRoot == NULL
            return True
        if not root or not subRoot: # If either one is NOT NULL
            return False
        # Both are not null, so we can safely check their values
        if root.val == subRoot.val:
            check = isSameTree(root, subRoot)
            if not check:
                # If isSameTree fails, we should check for other nodes if there could be subtrees there
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            else:
                return check
        # Otherwise, there could be subtrees elsewhere
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

"""
=========================================================
KEY LEARNINGS: Subtree of Another Tree (LeetCode 572)
=========================================================

CORE CONCEPTS:
1. Two Traversals at Once: This problem is a DFS inside a DFS. 
   The outer `isSubtree` function walks through every node in the 
   main tree. For every single node it visits, it triggers the 
   inner `isSameTree` function to do a structural check.
2. Time Complexity: $O(R * S)$ where R is the number of nodes in 
   the Root tree, and S is the number of nodes in the SubRoot. 
   In the worst case, we run a full `isSameTree` check on every 
   single node in the main tree.

GUIDING HINTS:
- Don't try to manually check `if root.val == subRoot.val` first. 
  Just delegate that job to `isSameTree()`. 
- The 3-Step Flow for `isSubtree`:
  1. Base cases (`if not subRoot: True`, `if not root: False`).
  2. The Match Check: `if isSameTree(root, subRoot): return True`
  3. The Recursive Search: `return isSubtree(left) or isSubtree(right)`
=========================================================
"""
