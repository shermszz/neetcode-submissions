# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we can run a simple inorder traversal and make sure that as we go, the numbers we encounter must be monotonically increasing.
        # At any point we encounter a value that is not in increasing sequence, we will immediately return false

        prev = -float('inf')
        def helper(root: Optional[TreeNode]) -> bool:
            nonlocal prev
            # Base case: If root is null, we return True (trivial base case)
            if not root:
                return True 
            
            if not helper(root.left):
                return False

            # Now, we check the middle value
            curr_val = root.val
            if curr_val <= prev:
                # This is where we stop
                return False
            # Otherwise, we update the previous value to be this next highest curr_value
            prev = curr_val 

            return helper(root.right)

        # create a recursive helper function here to determine whether it is a valid BST or not
        return helper(root)