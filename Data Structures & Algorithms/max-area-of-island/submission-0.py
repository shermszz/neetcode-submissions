class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        # Iterate through the entire grid.
        # On the first "1" that I see, I will run BFS on it to find the size of that island
        # Record the size of the island and compare it with max_area
            # Everytime we encounter an island, we flip its digit to 0, to mark as visited
        # Repeat for every unvisited "1"

        r, c = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(i, j, grid, local_area):
            nonlocal max_area
            queue = deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                # For each possible direction, if valid, check whether we can extend the island
                for dir in directions:
                    new_i, new_j = i + dir[0], j + dir[1]
                    if new_i >= 0 and new_i < r and new_j >= 0 and new_j < c:
                        if grid[new_i][new_j] == 1:
                            # We can extend the island, so we update local_area
                            grid[new_i][new_j] = 0
                            queue.append((new_i, new_j))
                            local_area += 1
            # At the end, we compare who has the biggest island so far
            max_area = max(max_area, local_area)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    local_area = 1
                    grid[i][j] = 0
                    bfs(i, j, grid, local_area)
        return max_area

"""
=========================================================
KEY LEARNINGS: Max Area of Island (LeetCode 695)
=========================================================

CORE CONCEPTS:
1. The "Scanner and Explorer" Pattern: Just like Number of Islands, 
   use a double `for` loop to scan. When you hit a "1", launch your 
   BFS Explorer to map the exact size of that specific island.
2. Local vs. Global Tracking: You need two variables: 
   - `max_area` (Global tracker sitting in the main function).
   - `local_area` (Local tracker specifically counting the island 
     your BFS is currently exploring).
3. Pure Functions: The cleanest way to pass data out of a BFS is to 
   have the BFS `return` the final `local_area` it calculated, instead 
   of using `nonlocal` to modify the global maximum from inside.

GUIDING HINTS & TRAPS AVOIDED:
- Space Optimization ("Sinking the Island"): By flipping the "1" to 
  a "0" the exact moment you visit it, you completely eliminate the 
  need for an O(R x C) `visited` array.
- The Start Value Trap: If your scanner finds a "1", the area is 
  already at least 1! Make sure your `local_area` starts at 1, not 0, 
  before you launch the BFS to check its neighbors.
=========================================================
"""