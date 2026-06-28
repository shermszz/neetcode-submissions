class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # One naive solution would be to iterate through each cell, if it is a 'O', we run BFS to see if it can escape to the walls
        # If it can escape, then it is not a surrounded region, otherwise we mark it as 'X'

        # Instead of running BFS so many times, we can start from the walls of the grid. 
        # From the walls of the grid, we run BFS from outside to find all the coordinates that are accessible via a '0' cell
        # Store all of these coordinates inside a hashset
            # OPTIMIZATION: Instead of having extra space to store, we can modify the board itself if we encounter a 'O' to change it to 'T'
        # Then, iterate through the grid once, if the coordinate is not inside the hashset, we mark it as an X

        queue = deque() # To store coordinates
        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                if i == 0 or j == 0 or i == r - 1 or j == c - 1:
                    # These are the edges of the board
                    queue.append((i, j))
        
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        # Run BFS on the queue elements, looking for a cell with '0' to continue expanding into the grid
        while queue:
            i, j = queue.popleft()
            # visited.add((i, j))
            if board[i][j] == 'X' or board[i][j] == 'T':
                continue
            
            # Otherwise, if it is a 'O', we need to save this coordinate as one that is not surrounded
            # remains.add((i, j))
            board[i][j] = 'T' # To temporarily mark this position as visited and later change back to 'O'
            
            # Then, check if there are any other 'O's that can escape through this
            for dir in directions:
                new_i, new_j = i + dir[0], j + dir[1]
                if new_i >= 0 and new_i < r and new_j >= 0 and new_j < c:
                    if board[new_i][new_j] == 'O':
                        queue.append((new_i, new_j))
        
        # Once we have our remains set populated, we can iterate through the grid once more and modify the coordinates that needs to be modified
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return

"""
=========================================================
KEY LEARNINGS: Surrounded Regions (LeetCode 130)
=========================================================

CORE CONCEPTS:
1. Reverse Flood Fill (Again!): When looking for things that "touch 
   the edge," don't search from the inside out. Launch your BFS from 
   all the valid edge cells simultaneously.
2. The 3-State In-Place Marker: To achieve O(1) auxiliary space 
   (excluding the queue), use a placeholder character to track state:
   - 'O' -> Unvisited land.
   - 'T' -> Safe land connected to the border.
   - 'X' -> Water / Captured land.

GUIDING HINTS & TRAPS AVOIDED:
- The Ping-Pong Trap: If you mutate the board instantly (changing 'O' 
  to 'T' the moment you add it to the queue), you naturally prevent 
  infinite loops because neighbors will no longer see an 'O'!
- Two-Pass Matrix Modification: First pass runs the BFS and places 
  all the 'T' markers. Second pass simply loops the matrix and 
  flips 'O' to 'X' and 'T' to 'O'.
=========================================================
"""
