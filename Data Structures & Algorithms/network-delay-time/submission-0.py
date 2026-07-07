class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # times = Directed Weighted graph
        # We need to find the single source shortest path to every node

        # First, we convert the edge list into an adj_list which is a hashmap of u : (v, weight)
        # Then, we create a minHeap to store the edges along with their weight
        # Create a visited set to track the nodes that we have visited.
        
        # We will perform lazy deletion in the heap. Any node we visit before, we skip, since this is a greedy solution

        adj_list = defaultdict(list)
        minHeap = []
        visited = set()

        for u, v, w in times:
            adj_list[u].append((v, w))

        # Initialize the starting point
        requiredTime = float('inf')
        heapq.heappush(minHeap, (0, k)) # starting point is node k. value at the start is the cumulative time needed to reach node k
        
        print("Adj_list", adj_list)
        while minHeap:
            print("current state of minHeap", minHeap)
            time_needed, u = heapq.heappop(minHeap)
            if u in visited: # We have seen and processed this node before, skip it
                continue
            visited.add(u)

            print("processing node", u)
            requiredTime = time_needed # Update the time needed to reach node u
            
            # Now process the neighbours
            print("neighbours of", u, "is", adj_list[u])
            for v, weight in adj_list[u]:
                if v not in visited:
                    print('adding', v, "to the min heap")
                    heapq.heappush(minHeap, (weight + time_needed, v))

        for i in range(1, n + 1):
            if i not in visited:
                print("returning -1 since", i, "is not in the set")
                return -1
        return requiredTime

"""
=========================================================
KEY LEARNINGS: Network Delay Time (LeetCode 743)
=========================================================

CORE CONCEPTS:
1. Dijkstra's Algorithm (Lazy Deletion): The ultimate solution for 
   Single-Source Shortest Path on a Weighted Graph. 
   - Use a Min-Heap (`heapq`).
   - Store cumulative distance: `(cumulative_dist, node)`.
   - Pop the smallest distance. If `node in visited`, skip it! 
     (This is the Lazy Deletion).
2. The Maximum is the Last: Because the Min-Heap processes nodes in 
   increasing order of distance, the distance of the LAST unvisited 
   node you pop is the maximum time it takes to traverse the graph.
3. Edge Weight Representation: When building your Adjacency List for 
   weighted graphs, store tuples: `adj[u].append((v, weight))`.

GUIDING HINTS & TRAPS AVOIDED:
- The Accumulation Trap: Never sum the weights as you pop them out 
  like a standard BFS counter. Distances must be cumulative *along the 
  path*, calculated before you push to the heap!
=========================================================
"""