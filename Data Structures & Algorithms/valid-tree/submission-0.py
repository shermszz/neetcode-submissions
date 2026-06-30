class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edges is an edge list
        # A valid tree has 2 conditions:
            # 1. No cycles -> Run DFS to check for cycles
            # 2. All nodes must be connected -> There must be exactly n - 1 edges

        # 1. Check if the graph can even be a valid tree
        if len(edges) != n - 1:
            return False
        
        # 2. Check for cycles by running DFS
        # Thing to note: If we reach here, that means a graph with n nodes and n - 1 edges if is a valid tree can never form a cycle
        # Hence, all we need to do is run DFS on all the nodes in the graph, and update a visited array
        # If the visited array did not visit all the nodes, that means the graph is disconnected and contains some cycle
        # First, we build our adj_list
        adj_list = defaultdict(list)
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0 for i in range(n)] # 0 - unvisited, 1 - visited
        def dfs(node):
            if visited[node] == 1:
                return 
            visited[node] = 1
            for neighbour in adj_list[node]:
                dfs(neighbour)
                
        dfs(0)
        for num in visited:
            if num == 0:
                return False
        return True
        


"""
=========================================================
KEY LEARNINGS: Graph Valid Tree (LeetCode 261)
=========================================================

CORE CONCEPTS:
1. The Tree Math Law: A valid tree of `n` nodes MUST have exactly 
   `n - 1` edges. If you check `len(edges) != n - 1` at the very top, 
   you instantly filter out all dense cycles and sparse disconnected graphs!
2. Undirected Adjacency Lists: The input `[u, v]` means the connection 
   goes BOTH ways. You must append to both: 
   `adj[u].append(v)` and `adj[v].append(u)`.
3. Reachability DFS: Because of the Tree Math Law, cycle detection 
   logic is no longer required. You just run a standard DFS from Node 0 
   and check if the number of visited nodes equals `n` at the end.

GUIDING HINTS & TRAPS AVOIDED:
- The Disconnected Cycle Trap: A graph with 4 nodes and 3 edges might 
  have a triangle cycle (3 nodes) and one completely isolated node. 
  Checking `len(edges) == n - 1` is not enough on its own; you MUST 
  verify that all components are connected (via DFS/BFS).
- The Directed Illusion Trap: Never assume edge lists are parent-to-child 
  unless the problem explicitly states it is a Directed Graph!
=========================================================
"""