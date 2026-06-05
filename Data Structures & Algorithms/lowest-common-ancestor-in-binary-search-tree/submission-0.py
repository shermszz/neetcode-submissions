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