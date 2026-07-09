class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Tickets is an edge list, each one being 3 uppercase letters long

        # First, build up an adjacency list
        adj_list = defaultdict(list)
        for u, v in tickets:
            adj_list[u].append(v)

        # For each list inside the adj_list, make it into a heap
        # This is to get the elements in lexographically smallest order
        for l in adj_list.values():
            heapq.heapify(l) 
        # print(adj_list)

        # The single source is always "JFK", so we start iterating from this 
        result = []
        
        def dfs(dest):
            neighbours = adj_list[dest]
            # print("Neighbours of", dest, "is", neighbours)
            while neighbours:
                n = heapq.heappop(neighbours)
                dfs(n)
            result.append(dest)

        dfs("JFK") # The starting single source
        result.reverse()
        return result
        
"""
=========================================================
KEY LEARNINGS: Reconstruct Itinerary (LeetCode 332)
=========================================================

CORE CONCEPTS:
1. Eulerian Path vs. Standard DFS: You are trying to use every EDGE 
   (ticket) exactly once, not visit every NODE (airport) once. 
   Therefore, DO NOT use a `visited` set for airports. You must 
   physically remove/pop the tickets from the graph as you use them.
2. Hierholzer's Algorithm (Post-Order DFS): A standard greedy DFS 
   will get stuck in dead-ends. Instead, use a Post-Order traversal: 
   an airport is only appended to the `result` list AFTER its ticket 
   heap is completely empty. 
3. The Reversal: Because dead-ends finish their function calls first, 
   they end up at the FRONT of your result list. Simply `reverse()` 
   the list at the end to get the perfect chronological itinerary.

GUIDING HINTS & TRAPS AVOIDED:
- The Lexicographical Requirement: Using `heapq` on the adjacency list 
  values is the perfect way to ensure you always attempt the 
  alphabetically smallest destination first. 
- The Workaholic Loop: Always use a `while` loop to exhaust edges 
  in Eulerian path problems, not an `if` statement!
=========================================================
"""