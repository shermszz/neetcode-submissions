class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # This is a MST problem, let's use Prim's algorithm to solve this
        num_nodes = len(points)
        visited = set() # To keep track of the number of nodes we have visted

        # We need to iterate through each point, pick out the one with the smallest manhatten distance, and then process that one
        # We need to build a complete graph of this first to get the cost of from each point to every other point
        adj_list = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i][0], points[i][1]
            for j in range(len(points)):
                if i == j: 
                    continue
                xj, yj = points[j][0], points[j][1]
                dist = abs(xi - xj) + abs(yi - yj) # This is the cost from (xi, yi) <--> (xj, yj)
                adj_list[i].append((dist, j))

        minHeap = []
        heapq.heappush(minHeap, (0, 0)) # Push the first point and its cost which is 0
        min_cost = 0

        while minHeap and len(visited) != num_nodes:
            cost, idx = heapq.heappop(minHeap)
            if idx in visited:
                continue
            visited.add(idx)
            min_cost += cost # This is the minimum to get to node at [idx], so we add to the cost
            for cost, next_node in adj_list[idx]:
                if next_node not in visited:
                    heapq.heappush(minHeap, (cost, next_node))

        return min_cost

"""
=========================================================
KEY LEARNINGS: Min Cost to Connect All Points (LeetCode 1584)
=========================================================

CORE CONCEPTS:
1. Minimum Spanning Tree (MST) vs. Shortest Path: 
   - Dijkstra (Shortest Path) = The GPS. Find the fastest route from 
     A to B for ONE person.
   - Prim / Kruskal (MST) = The Power Grid. Connect ALL nodes together 
     using the absolute minimum total weight/wire possible.
2. Prim's Algorithm (The Expanding Blob): Node-centric. Start at one 
   arbitrary node, throw its edges into a GLOBAL Min-Heap, and constantly 
   pop the cheapest edge that connects a new node to your growing grid.
3. Kruskal's Algorithm (The Edge Picker): Edge-centric. Sort all edges 
   globally from smallest to largest, then use Union-Find to safely merge 
   them, throwing away edges that cause cycles (Redundant Connections!).

GUIDING HINTS & TRAPS AVOIDED:
- The "Tunnel Vision" Bug: In Prim's, you cannot just look at the edges 
  of the node you *just* visited. You must use ONE Global Min-Heap so 
  the algorithm remembers cheap edges from nodes visited earlier!
- The O(N^2) Memory Trap: For coordinate-based complete graphs, DO NOT 
  build an Adjacency List. Storing 1,000,000 edges will cause a Memory 
  Limit Exceeded error. Calculate the Manhattan distances on-the-fly!
- Heap Bloat Prevention: Always check `if next_node not in visited` 
  BEFORE pushing to the heap to keep it lean and fast.
=========================================================
"""
        