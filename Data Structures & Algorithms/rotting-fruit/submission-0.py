class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Minimum possible minutes means we want to find the SSSP of rotting oranges to spread to everyone

        # In such a case, we first iterate through the grid, Record a few things:
            # 1. The total count of fresh oranges -> at the end if count > 0, means there is a fresh orange that cannot be rotten, return -1
            # 2. All the rotten oranges, put them into a queue
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0)) # Tuple of (i, j, time), where time == 0 initially
    
        # Once we have the queue of all initial rotten oranges, we start to infect in all 4 valid directions
        # To keep track of the time, we can store the orange's positions as a tuple of (i, j, time)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time_required = 0
        while queue:
            i, j, curr_time = queue.popleft()
            time_required = curr_time
            for dir in directions:
                new_i, new_j = i + dir[0], j + dir[1]
                if new_i >= 0 and new_i < rows and new_j >= 0 and new_j < cols:
                    # Within a valid bound, we check if there are any fresh oranges to rot
                    # If there are, we change its value to 2, decrease fresh_count and then add this position into the queue with an updated time stamp
                    if grid[new_i][new_j] == 1:
                        fresh_count -= 1
                        grid[new_i][new_j] = 2 # Become rotten
                        queue.append((new_i, new_j, curr_time + 1))
        return time_required if fresh_count <= 0 else -1

"""
=========================================================
KEY LEARNINGS: Rotten Oranges (LeetCode 994)
=========================================================

CORE CONCEPTS:
1. Multi-Source BFS (Again!): Perfect application of queuing all 
   starting points (rotten oranges) at the very beginning to simulate 
   simultaneous, outward spread.
2. The `target_count` Tracker: Instead of rescanning the grid at the 
   end to see if any 1s are left, count the 1s during the initial 
   setup. Decrement the count as you infect them. If `count > 0` at 
   the end, you return -1. Massive time saver!
3. Level-Order BFS vs. Queue State: You have two ways to track time:
   - Store it in the queue: `queue.append((r, c, time))`
   - Process by levels: `for _ in range(len(queue)):` per loop. 
     (Both are O(N), choose whichever makes more sense to your brain!)

GUIDING HINTS & TRAPS AVOIDED:
- Early Termination: If `fresh_count` hits 0, you can technically 
  break out of the BFS early to save a few CPU cycles!
- The Zero Fresh Edge Case: If the grid has 0 fresh oranges at the 
  very beginning, your code correctly returns 0 minutes instead of -1 
  because of the `if fresh_count <= 0` logic at the bottom.
=========================================================
"""   