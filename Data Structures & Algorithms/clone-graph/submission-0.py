"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Deep copy means we want the same values and structure, but a completely different object altogether
        if not node:
            return None
        
        old_to_new = {} # Keep a hashmap of {old node -> new node}
        old_to_new[node] = Node(node.val, None)
        queue = deque([node])
        
        while queue:
            curr_node = queue.popleft()
            curr_val, curr_neighbours = curr_node.val, curr_node.neighbors
            clone_node = old_to_new[curr_node] # Get the cloned node of the one we are inspecting right now

            for n in curr_neighbours:
                if n not in old_to_new: # If this original node does not yet exist in the hash map
                    new_node = Node(n.val, None)
                    old_to_new[n] = new_node # immediately create an entry for it
                    queue.append(n)
                clone_node.neighbors.append(old_to_new[n]) # For the cloned node we are inspecting, append the clone to it that can be retrieved by the hash map

        return old_to_new[node]

"""
=========================================================
KEY LEARNINGS: Clone Graph (LeetCode 133)
=========================================================

CORE CONCEPTS:
1. The "Registry" Pattern (Hash Map): For any problem involving 
   "Deep Copies" with complex pointers (Clone Graph, Copy List with 
   Random Pointer), you MUST use a Hash Map of `{Original_Node : Cloned_Node}`.
   This prevents infinite loops and allows you to attach back-edges 
   to nodes you have already processed.
2. Single-Pass BFS: You can clone and connect a graph simultaneously. 
   When you pop an original node, fetch its clone from the Registry. 
   Then, loop through the original neighbors. If a neighbor isn't in 
   the Registry, build it and queue it. Finally, attach the neighbor's 
   clone to the current clone.

GUIDING HINTS & TRAPS AVOIDED:
- The Scope Trap: Do not try to append a local variable (like `new_node`) 
  inside the neighbor loop, because you will skip already-visited 
  neighbors. ALWAYS append by fetching from the registry: 
  `clone.neighbors.append(registry[neighbor])`.
- Shallow Copying Trap: Never pass the original node's neighbor list 
  into the new node's constructor, or you will contaminate the New 
  Graph with Old Graph pointers! Always initialize clones with an 
  empty neighbors array.
=========================================================
"""
