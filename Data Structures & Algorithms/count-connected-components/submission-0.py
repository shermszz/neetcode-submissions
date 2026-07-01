class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # edges == Edge list
        # To find the number of connected components, we can do a simple DFS
        # everytime we need to restart our DFS in a for loop, we can increment the number of connected components by one

        # First, we need to convert the edge list into an adjacency list so that it is more efficient to traverse
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u) # undirected graph
        
        # Then, we set up num_connected_components and a visited array 
        num_connected_components = 0
        visited = [0 for i in range (n)] # 0 - unvisited, 1 - visited

        # For every single node, we will run DFS if not already visited.
            # Within this for loop, if DFS is triggered, we are in a new connected component
        def dfs(node):
            if visited[node] == 1:
                # Visited before
                return
            visited[node] = 1 # visited this node
            for neighbour in adj_list[node]:
                dfs(neighbour)

        for i in range(n):
            if visited[i] == 1:
                continue
            num_connected_components += 1
            dfs(i)
        
        return num_connected_components        

"""
=========================================================
KEY LEARNINGS: Number of Connected Components (LeetCode 323)
=========================================================

CORE CONCEPTS:
1. The "Bucket of Paint" BFS/DFS: To count isolated islands or 
   components, loop through every single node. If a node is 
   unvisited, increment your counter by 1, then launch a full 
   BFS/DFS from that node to mark its entire connected component 
   as visited.
2. Undirected Adjacency Lists (Review): Always remember to append 
   in both directions: `adj[u].append(v)` and `adj[v].append(u)`.

GUIDING HINTS & TRAPS AVOIDED:
- The Disconnected Setup Trap: You successfully avoided launching DFS 
  from just Node 0. By wrapping the DFS launch inside a `for i in range(n):` 
  loop, you guaranteed that completely isolated nodes (or separate clusters) 
  would be independently discovered and counted!
=========================================================
"""