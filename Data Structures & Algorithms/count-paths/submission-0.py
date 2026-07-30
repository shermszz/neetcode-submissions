class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # We need to have a 2D DP grid. 
        # At each cell, we want to know how many unique ways there are to reach that cell
        # Base case: the first cell at [0,0] starts at 1 way to reach that square
        dp_grid = [[0 for _ in range(n)] for _ in range(m)]
        dp_grid[0][0] = 1
        # print(dp_grid)

        for i in range(m):
            for j in range(n):
                # Initialize the corners of the grid where i = 0 or j = 0 to be 1, since there is only 1 way to reach the corners from the corner (0,0)
                if i == 0 or j == 0:
                    dp_grid[i][j] = 1
                    continue
                
                # The man must have come from a path above him or from his left
                # Hence, we want the total number of unique paths from his left and from his right to update the current number of unique ways to reach the current cell
                
                left_paths = dp_grid[i][j - 1]
                # print("Number unique paths from the left", left_paths)
                above_paths = dp_grid[i - 1][j]
                # print("Number of unique paths from above", above_paths)
                dp_grid[i][j] = left_paths + above_paths

        return dp_grid[m - 1][n - 1]
        
