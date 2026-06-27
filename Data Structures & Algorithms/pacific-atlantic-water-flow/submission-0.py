class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # To the pacific ocean --> Up or left (until out of bounds)
        # To the Atlantic ocean --> Bottom or right (until out of bounds)

        # For each node, check if it can flow to the pacific AND atlantic
        # Naive approach -> run bfs_to_pacific and bfs_to_atlantic for each node in the grid

        # Instead, lets check from each part of the ocean, where can we possibly reach in the grid
        # From the Pacific, find all the coordinates that it can reach. 
            # (Must check in reverse order in terms of water flow), from low --> high
        # From the Atlantic, find all coordinates that it can also reach.
        # Find all the common coordinates from both lists. 
        r, c = len(heights), len(heights[0])
        pacific_queue, atlantic_queue = deque(), deque()
        atlantic_visited,  pacific_visited = set(), set()

        # Set up the pacific queue with all the edges that touch the pacific ocean first
        for i in range(r):
            for j in range(c):
                if i == 0 or j == 0:
                    pacific_queue.append([i, j])
                    pacific_visited.add((i, j))
                if i == r - 1 or j == c - 1:
                    atlantic_queue.append([i, j])
                    atlantic_visited.add((i, j))
        print("Pacific queue", pacific_queue)
        print("atlantic queue", atlantic_queue)
        
        def bfs(queue, visited_set):
            directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
            while queue:
                curr_i, curr_j = queue.popleft()
                curr_val = heights[curr_i][curr_j]
                for dir in directions:
                    new_i, new_j = curr_i + dir[0], curr_j + dir[1]
                    if new_i >= 0 and new_i < r and new_j >= 0 and new_j < c:
                        # Check whether we are allowed to traverse to that cell if the cell value is HIGHER or not
                        new_val = heights[new_i][new_j]
                        if curr_val <= new_val and (new_i, new_j) not in visited_set:
                            # Then we know from this new cell, we can reach the ocean
                            visited_set.add((new_i, new_j))
                            queue.append([new_i, new_j])
        # Now, we run multi-source BFS on the pacific first to see where are all the coordinates it can visit
        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)

        # Once we have both sets fully filled, we just need to find the common coordinates inside the sets
        result = []
        for coord in pacific_visited:
            if coord in atlantic_visited:
                # save this coordinate as a list
                i, j = coord
                result.append([i, j])
        return result

"""
=========================================================
KEY LEARNINGS: Pacific Atlantic Water Flow (LeetCode 417)
=========================================================

CORE CONCEPTS:
1. Reverse Flood Fill: When a problem asks "which cells can reach 
   the edge," it is almost always faster to ask "which cells can the 
   edge reach?" Start at the destinations and flow backwards.
2. Dual Visited Sets: By maintaining two separate sets (`pacific_visited` 
   and `atlantic_visited`), you ensure that each ocean processes a 
   cell a maximum of ONE time. Total time complexity becomes O(R x C).
3. Set Intersection: The final answer is simply the intersection of 
   the two sets. (e.g., coordinates that were successfully flooded by 
   BOTH oceans).

GUIDING HINTS & TRAPS AVOIDED:
- The Ping-Pong Trap (Again!): Even in a reverse flood fill, water 
  can flow back and forth between two flat cells of the same height. 
  You MUST check `if (new_i, new_j) not in visited` before appending 
  to the queue!
- Queue Initialization: Don't launch the BFS one border cell at a time. 
  Pre-load the queues with ALL the respective border cells first, so 
  they expand inward as one massive, synchronized wave.
=========================================================
"""