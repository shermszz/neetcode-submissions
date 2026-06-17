class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]# Up, Down, Left, Right
        visited = set() # To keep track of the cells that were visited
        
        def dfs(row, col, index):
            # 1. Check if we have already found the word
            if index == len(word):
                return True
            
            # 2. Check if row, col is even in range and if it has been visited before
            if row < 0 or row >= r or col < 0 or col >= c or (row, col) in visited:
                return False
            
            # 3. Check if the current letter we are on is matching or not
            if board[row][col] != word[index]:
                return False
            else:
                index += 1 # Found one correct letter
            
            visited.add((row, col))
            
            # 4. Check every other direction
            res = False
            for i, j in directions:
                new_i, new_j = row + i, col + j
                res = res or dfs(new_i, new_j, index)
            visited.discard((row, col))
            return res

        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0): # Run DFS on every single element
                    return True
        return False

"""
=========================================================
KEY LEARNINGS: Word Search (LeetCode 79)
=========================================================

CORE CONCEPTS:
1. 2D Grid Backtracking: Requires two distinct parts:
   - The Scanner (Double `for` loop to find the starting point).
   - The Explorer (DFS function to recursively check neighbors).
2. The `visited` Set: Prevents infinite loops and reusing the same 
   cell. Add the cell before branching, and REMOVE it after branching 
   so parallel universes can use it.
3. The 3 Bouncers of Grid DFS: At the top of your function, always check:
   - Out of bounds? 
   - Already visited? 
   - Wrong target? 
   If any of these are true, instantly `return False`.

GUIDING HINTS & TRAPS AVOIDED:
- Base Case Order: ALWAYS check if you reached the target length 
  (`index == len(word)`) BEFORE you check the board boundaries. 
  Otherwise, the final successful step will accidentally trigger an 
  "Out of Bounds" or "Wrong Letter" error!
- Listen to the Explorer: In your outer Scanner loops, don't just 
  call `dfs()`. Check `if dfs(): return True` so you can instantly 
  halt the program the moment the word is found.
=========================================================
"""