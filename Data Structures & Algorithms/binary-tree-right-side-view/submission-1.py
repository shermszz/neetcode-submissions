# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # Traverse the tree level by level using BFS
        res = []
        queue = deque([root])
        
        while queue:
            curr_len = len(queue)
            if curr_len > 1:
                # We should remove curr_len - 1 nodes and then append that last one
                for _ in range(curr_len - 1):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                last_node = queue.popleft() # The last node for that particular level
                res.append(last_node.val)
                if last_node.left:
                    queue.append(last_node.left)
                if last_node.right:
                    queue.append(last_node.right)
            elif curr_len == 1:
                # This is the only node on that level, it is thus visible
                visible = queue.popleft()
                res.append(visible.val)
                if visible.left:
                    queue.append(visible.left)
                if visible.right:
                    queue.append(visible.right)
        return res
    