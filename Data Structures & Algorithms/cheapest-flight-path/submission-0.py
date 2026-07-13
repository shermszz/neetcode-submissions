class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # n flights, 0 to n - 1
        # flights is a directed weighted edge list

        # src = starting, dst = destination airport, k = max number of stops to make
        # Instead of just finding the cheapest path, we need to also consider the number of stops to make

        #First, lets convert the edge list into an adj_list for optimal traversal
        adj_list = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((w, v)) # Append the weight first in the tuple
        
        print("adj_list", adj_list)
        
        # Instead of only considering the cheapest cost, we can run a standard BFS to adhere to the K stops limit
        queue = deque([[0, src, k + 1]])
        costs = [float('inf') for _ in range(n)] # Initially store the cost to all destinations as infinity first
        costs[src] = 0 # The source will have a cost of 0 first
        print("Initial state of queue", queue)
        while queue:
            curr_cost, curr_airport, steps_remaining = queue.popleft()
            print("Currently processing", curr_airport, "with", steps_remaining, "steps remaining")
            if curr_airport == dst:
                if curr_cost < costs[dst]:
                    costs[dst] = curr_cost
                continue
            if steps_remaining == 0:
                # If run out of steps, we are not at the destination, we dont have to do anything anymore
                continue                

            # Process all the neighbours
            for travel_cost, neighbour in adj_list[curr_airport]:
                if curr_cost + travel_cost < costs[neighbour]:
                    costs[neighbour] = curr_cost + travel_cost # We have found a cheaper alternative.
                    queue.append((costs[neighbour], neighbour, steps_remaining - 1))
                    
                    print("Added to the queue airport number", neighbour, "with", steps_remaining, "steps remaining" )
        return -1 if costs[dst] == float('inf') else costs[dst]

"""
=========================================================
KEY LEARNINGS: Cheapest Flights Within K Stops (LeetCode 787)
=========================================================

CORE CONCEPTS:
1. Bounded Shortest Path: Standard Dijkstra fails because it ignores 
   stop limits. Standard BFS fails because it ignores costs. The solution 
   is a "Cost-Aware BFS" (effectively Bellman-Ford / SPFA bounded by K).
2. Passenger Receipts (Queue State): Instead of just storing the node, 
   the queue must carry the state of the journey: `(cost_so_far, node, 
   steps_remaining)`.
3. The K-Stop Math: K stops mathematically means K + 1 total flights/edges. 
   Initialize the queue with K + 1 steps remaining, and decrement by 1 
   for every edge traversed.

GUIDING HINTS & TRAPS AVOIDED:
- The Premature Return Trap: In a weighted BFS, reaching the destination 
  does NOT mean you found the cheapest path, it just means you found the 
  shortest path by edges. Record the cost, but let the BFS finish running!
- The Global Visited Trap: A simple True/False visited set will block 
  cheaper, longer paths. Instead, use a `costs` array. Only revisit a 
  node if the new path is strictly CHEAPER than the recorded cost.
=========================================================
"""