# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good_nodes = 0
        
        # Run a DFS on the root, keeping track of the maximum value along a path to the leaf
        def dfs(node, max_so_far):
            nonlocal good_nodes
            
            if not node:
                return
            
            if node.val >= max_so_far:
                max_so_far = node.val
                good_nodes += 1
            
            # If node x is less than maximum, that means there is a node above it that is bigger, hence do not add to good_nodes count 
            
            dfs(node.left, max_so_far) # Continue checking the left side
            dfs(node.right, max_so_far) # Continue checking the right side
        
        dfs(root, root.val)
        return good_nodes