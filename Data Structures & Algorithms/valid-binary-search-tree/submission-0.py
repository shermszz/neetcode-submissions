# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Simply run an inorder traversal.
        # If at any point the node to be added is not in sorted ascending order, return False
        prev = -float('inf')
        def inorder(node):
            nonlocal prev

            if not node:
                return
    
            inorder(node.left)

            if prev != -float('inf'):
                # This is NOT the first node to be added, so we must check
                if node.val <= prev:
                    # Immediately we know it is not a valid BST
                    # Give it a dirty value like infinity to indicate False later
                    prev = float('inf')
                else:
                    prev = node.val # Update the value
            else:
                # First node to be added, so we just update
                prev = node.val
            
            inorder(node.right)
        inorder(root)
        return prev != float('inf')


