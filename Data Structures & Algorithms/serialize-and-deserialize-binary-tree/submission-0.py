# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            nonlocal res
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Given the data from our serialized tree, which is an array of strings in PREORDER
        # Since the preorder traversal already includes all the NULL values, we can uniquely recreate the binary tree
        arr = data.split(",") # Forms back the array 
        if arr[0] == "null":
            return None # There is no tree to deserialize
        i, x = 0, len(arr) # To traverse the array
        def dfs(string_val):
            nonlocal arr, i, x
            if string_val == "null":
                return None

            val = int(string_val)
            node = TreeNode(val, None, None)
            if i < x - 1:
                i += 1
            node.left = dfs(arr[i])
            if i < x - 1:
                i += 1 
            node.right = dfs(arr[i])
            return node

        root = dfs(arr[0])
        return root
        
        



