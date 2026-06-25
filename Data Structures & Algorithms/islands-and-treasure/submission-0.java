class Solution {
    public void islandsAndTreasure(int[][] grid) {
        int rows = grid.length; int cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        // Iterate through the grid once through first, and then record all the treasure's positions
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 0) {
                    // This is a treasure, record its position and initialize a step count of 0
                    int[] treasurePosition = new int[]{i, j, 0};
                    queue.add(treasurePosition);
                }
            }
        }

        // We have all positions of all treasures, now we iterate thorugh the queue until we find the step count for every position of the landmass
        // We can run simple BFS since it is unweighted graph, default the minimum distance to the nearest treasure
        int[][] directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0]; int c = curr[1]; int curr_dist = curr[2];
            for (int[] dir : directions) {
                int new_r = r + dir[0]; int new_c = c + dir[1];
                if (new_r >= 0 && new_r < rows && new_c >= 0 && new_c < cols && grid[new_r][new_c] != -1) {
                    //Do a terminating check here: If value at this column is a land mass, we have found the minimum distance
                    if (grid[new_r][new_c] == Integer.MAX_VALUE) {
                        //Modify the grid in place with the curr_dist + 1
                        grid[new_r][new_c] = curr_dist + 1;
                        queue.add(new int[]{new_r, new_c, curr_dist + 1});
                    } 
                    //Otherwise it is a cell that has been visited before, we also ignore it
                }
            }
        }
        return;
    }
}

/* 
=========================================================
KEY LEARNINGS: Islands and Treasure / Walls and Gates (LeetCode 286)
=========================================================

CORE CONCEPTS:
1. Multi-Source BFS: When a problem asks for the "shortest distance 
   from any target," do NOT run a BFS from every starting point. 
   Instead, put ALL targets (e.g., all treasures) into the queue at 
   the very beginning. They will expand outward simultaneously, 
   guaranteeing the shortest path wins.
2. The Inverse Search: Sometimes it is much faster to start at the 
   destination and walk backwards to the start.
3. The "Grid as Visited/Distance" Trick: If you are looking for 
   distances, and empty cells are initialized to infinity 
   (Integer.MAX_VALUE), you do not need a `visited` set or a step 
   counter in your queue. The grid value `grid[r][c]` tracks both!

GUIDING HINTS & TRAPS AVOIDED:
- The Overlapping Path Trap: If multiple treasures reach the same 
  empty room, how do we prevent them both from overwriting it? 
  Because BFS guarantees the shortest path is found first, the moment 
  a room changes from `MAX_VALUE` to a number, it is permanently 
  locked in. Any slower path arriving later will see it's no longer 
  `MAX_VALUE` and safely ignore it.
=========================================================
*/
