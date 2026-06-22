class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """ We can iterate through the grid. 
        If we find a "1", we increment a counter, and then run BFS on it to find all adjacent 1s. 
        Keep a visited grid as well to track what has been tracked. 
        """
        r, c = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def bfs(grid, i, j):
            # grid refers to the entire grid given in the question
            # visited is the 2D array that tell us whether a particular node has been visited before
            # i, j are the row, col coordinates
            queue = deque([(i, j)])

            while queue:
                print("Curr state of queue", queue)
                i, j = queue.popleft()
                for dir in directions:
                    new_i, new_j = i + dir[0], j + dir[1]
                    if new_i >= 0 and new_i < r and new_j >= 0 and new_j < c:
                        # Within bounds of the board, then we check if there are more islands to connect
                        if grid[new_i][new_j] == "1":
                            queue.append((new_i, new_j))
                            grid[new_i][new_j] = 0
        # Iterate through the grid to find the number of islands
        num_islands = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    num_islands += 1 # For every distinct new island we see, we add to the count
                    grid[i][j] = 0 # Destroy the island after we visit it once
                    bfs(grid, i, j)
        return num_islands

"""
=========================================================
KEY LEARNINGS: Number of Islands (LeetCode 200)
=========================================================

CORE CONCEPTS:
1. Iterate + Traverse Pattern: For disconnected graph problems, use a 
   double `for` loop to scan the grid. When you hit a valid starting 
   condition (like land), launch your BFS/DFS.
2. The Ping-Pong Trap: If you do not mark nodes as visited the MOMENT 
   you put them in the queue, your BFS will bounce back and forth 
   between neighbors infinitely.
3. In-Place Graph Modification ("Sinking the Island"): If you are 
   allowed to modify the input grid, you can optimize Space Complexity 
   by changing the grid values (e.g., "1" to "0") to mark them as 
   visited, completely removing the need for a separate boolean array!

GUIDING HINTS & TRAPS AVOIDED:
- The Queue Trigger: Always mark a node as visited/sunk exactly when 
  you `append` it to the queue, NOT when you `pop` it. If you wait 
  until you pop it, other neighbors might accidentally add it to the 
  queue multiple times in the meantime!
- Type Consistency: Keep the data types of the grid uniform. If it 
  starts as strings, replace visited nodes with strings.
=========================================================
"""
