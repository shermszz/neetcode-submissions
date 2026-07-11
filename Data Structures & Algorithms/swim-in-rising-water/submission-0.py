class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # grid is like a weighted adjacency matrix.
        # We need to find a path with the lowest maximal rain water level required
        rain_level_required = 0 # max rain level required

        # the goal is to reach (row - 1, col - 1) in the least amount of time possible
        # Each weight represents the amount of time needed to wait in order to flow to that coordinate
        minHeap = [(grid[0][0], 0, 0)] # Start with weight 0, then coordinate (0, 0)
        directions = { (-1, 0), (1, 0), (0, -1), (0, 1) } # NSEW directions
        visited = {(0, 0)}

        while minHeap:
            cost, curr_x, curr_y = heapq.heappop(minHeap)
            print("Processing square with cost", cost, "at pos (",curr_x, curr_y, ")")

            rain_level_required = max(rain_level_required, cost) # Track what is the greatest cost needed so far

            if curr_x == row - 1 and curr_y == col - 1:
                return rain_level_required
        
            for dir in directions:
                new_x, new_y = curr_x + dir[0], curr_y + dir[1]
                if new_x >= 0 and new_y >= 0 and new_x < row and new_y < col and (new_x, new_y) not in visited:
                    # If within a valid region, and also not visited before
                    visited.add((new_x, new_y))
                    heapq.heappush(minHeap, (grid[new_x][new_y], new_x, new_y))
        return rain_level_required

"""
=========================================================
KEY LEARNINGS: Swim in Rising Water (LeetCode 778)
=========================================================

CORE CONCEPTS:
1. Matrix as a Graph: A 2D grid is just a graph where each cell has 
   up to 4 edges (up, down, left, right).
2. Bottleneck Path (Prim's/Dijkstra on Grid): When you need to minimize 
   the MAXIMUM weight on a path, use a Min-Heap. Always pop the 
   currently available cell with the lowest height. Keep a running 
   `max()` of the heights you process.
3. Early Exit: In Single-Pair Shortest Path problems (Start to End), 
   you can safely `return` the exact moment your target coordinates 
   are POPPED from the heap.

GUIDING HINTS & TRAPS AVOIDED:
- The Initial Cost Trap: Never blindly initialize the heap with 0 cost. 
  If you are standing on `grid[0][0]`, the starting cost is `grid[0][0]`.
- Matrix Heap Bloat: Because path accumulation doesn't matter here (we 
  just want to unlock cells), you can mark cells as `visited` at the 
  exact moment you PUSH them to the heap. This prevents duplicate 
  coordinates from bloating the queue!
=========================================================
"""