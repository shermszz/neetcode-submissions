class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # There is a new algorithm called leaf peeling algorithm
        # In this algorithm, we will build up a queue to store the "leafs" of the graph, those with degree == 1
        # Since this is an undirected graph, we no longer look at those with in-degree = 0, but just degree = 1, beacuse that means it is a leaf
        # We slowly accumulate and remove leaf nodes from the queue and adding new leafs until the queue is empty
        # Then, we iterate through edges backwards, finding the first edge whose degree[u] and degree[v] are both > 1. 

        adj_list = defaultdict(list)
        degrees = [0 for i in range(len(edges) + 1)] # To record the degree of each node from 1 to n
        for u, v in edges:
            adj_list[u].append(v)
            degrees[u] += 1
            adj_list[v].append(u)
            degrees[v] += 1
        print("Adjacency list", adj_list)
        print("Degrees", degrees)

        # Now, iterate through degrees from 1 to n, finding any node whose degree = 1, which means they are a leaf node
        queue = deque()
        for i in range(1, len(degrees)):
            if degrees[i] == 1:
                queue.append(i)
        
        # Run BFS on the queue, removing the leaf, then decrmeneting the degree count of its neighbours
        while queue:
            curr_node = queue.popleft()
            degrees[curr_node] -= 1
            for neighbour in adj_list[curr_node]:
                if degrees[neighbour] > 0:
                    # Reduce the degree of the neighbour if the neighbour still exists
                    degrees[neighbour] -= 1
                    if degrees[neighbour] == 1:
                        # If it becomes a new leaf, add it back to the queue
                        queue.append(neighbour)
        
        # Once the loop terminates, we are left with a graph that is a cycle
        # Then, all we need to do is iterate through the edge list backwards to find the latest edge that contributed to the cycle
        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i][0], edges[i][1]
            if degrees[u] > 1 and degrees[v] > 1:
                return [u, v]
        return [0, 0] # Should never reach here

"""
=========================================================
KEY LEARNINGS: Redundant Connection (Leaf Peeling) 
=========================================================

CORE CONCEPTS:
1. Leaf Peeling (Undirected Topo-Sort): You can isolate cycles in an 
   undirected graph by aggressively destroying all the branches. 
   Initialize a queue with all nodes of `degree == 1`. 
2. The Chain Reaction: When you pop a leaf, you reduce its neighbors' 
   degrees by 1. If a neighbor becomes a 1, it is a new leaf! Add it 
   to the queue.
3. The Cycle Remnant: When the queue naturally empties, every node 
   that was part of a branch will have a degree of 0. The ONLY nodes 
   left with `degree > 1` are the nodes trapped in the cycle!

GUIDING HINTS & TRAPS AVOIDED:
- The Python Range Trap: `range(start, stop, -1)` stops strictly 
  BEFORE the `stop` index. To include index 0, your stop must be -1.
- The "Ghost Neighbor" Phenomenon: Adjacency lists don't delete 
  connections just because a node was processed. Protect your logic 
  by ensuring you only decrement degrees of neighbors that are still 
  greater than 0.
=========================================================
"""