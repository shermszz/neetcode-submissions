# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Do a preorder traversal to grab the nodes in that order into a string 
        res = []
        def dfs_preorder(node):
            nonlocal res
            if not node:
                res.append("null")
                return
            res.append(str(node.val)) # Append first, then check left, then check right (preorder style)
            dfs_preorder(node.left)
            dfs_preorder(node.right)
        dfs_preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # We are able to deserialize a binary tree using preorder only because of the "null" values that are intentionally inserted when we serialize the binary tree
        arr = data.split(",") # To get the array of strings back 

        # KEY LEARNING HERE: instead of manually using indices to traverse the array, use Python's ITERATOR
        iter_arr = iter(arr) # Kinda initializes "i = 0" and will keep track of this counter internally

        def dfs():
            val = next(iter_arr)

            if val == "null":
                return None
            
            node = TreeNode(int(val), None, None)
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
=========================================================
KEY LEARNINGS: Serialize & Deserialize Binary Tree (LeetCode 297)
=========================================================

CORE CONCEPTS:
1. The Power of Nulls: A standard Pre-order traversal loses the 
   shape of a tree. But a Pre-order traversal that explicitly 
   records `null` nodes perfectly preserves the shape! No In-order 
   array is needed.
2. The Assembly Line (Deserialization): Since Pre-order is 
   [Root, Left, Right], you can safely read the string strictly 
   left-to-right. 

GUIDING HINTS:
- Serialize: Use a standard Pre-order DFS, appending `str(node.val)` 
  or `"null"`. Join with commas at the end.
- Deserialize: Split by commas, and convert to an `iter()` (or `deque`).
- Inside `dfs()`: Pop the next value. If it's `"null"`, return `None`. 
  Otherwise, create the Node, call `dfs()` for the left child, call 
  `dfs()` for the right child, and return the Node.
=========================================================
"""