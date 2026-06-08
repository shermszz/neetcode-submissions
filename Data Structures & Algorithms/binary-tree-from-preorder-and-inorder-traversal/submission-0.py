# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # The thing to note is that the first node of preorder is the root
        # Then, we look at the inorder to determine the nodes to the left and right of that root node
        inorder_map = { num : index for index, num in enumerate(inorder)} # Create a hashmap of the inorder for O(1) lookup
        
        preorder_idx = 0

        def array_to_tree(in_left, in_right):
            nonlocal preorder_idx
            # Base case
            if in_left > in_right:
                return None
            
            # Get the current root node using the preorder_idx
            root_val = preorder[preorder_idx]
            preorder_idx += 1
            root = TreeNode(root_val, None, None)

            root.left = array_to_tree(in_left, inorder_map[root_val] - 1)
            root.right = array_to_tree(inorder_map[root_val] + 1, in_right)

            return root
        
        return array_to_tree(0, len(inorder) - 1)

"""
=========================================================
KEY LEARNINGS: Construct Binary Tree from Preorder & Inorder
=========================================================

CORE CONCEPTS:
1. Array Roles: `preorder` tells you WHO the root is (always the 
   first element). `inorder` tells you WHERE the left/right 
   subtrees are (everything left of the root is the left subtree).
2. The Global Pointer: Because preorder is perfectly sequential 
   [Root, Left..., Right...], you can just use a global index that 
   ticks up by 1 every time you create a node.
3. Trust the Return: Don't pass `root` into the helper function. 
   Let the helper build its own root, attach its children using 
   recursive calls, and `return root` to its parent.

GUIDING HINTS:
- Pre-compute an `inorder_map = {val: idx}` for O(1) lookups.
- Pass `in_left` and `in_right` pointers to track the current 
  valid subarray bounds, preventing O(N) array slicing.
- Base Case: `if in_left > in_right: return None`
- Left Child: `(in_left, mid - 1)`
- Right Child: `(mid + 1, in_right)`
=========================================================
"""