class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        GOAL: For the given word, we need to find whether or not the entire word can be formed from its neighbours that are veritcally or horizontally adjacent (left, right, up, down) directions

        We can iterate through the board, and everytime we encounter a matching character for the first letter, we will trigger a DFS algorithm to find any matching next letters.
        While we search, we need to mark the current cell that we came from as visited since we cannot go back there to fill up subsequent letters
        """
        
        rows, cols = len(board), len(board[0])
        def dfs(r, c, index):
            if index == len(word):
                return True
            
            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]):
                return False
            
            # 1. Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#" # Temporarily mark this cell as visited

            # 2. Dive all 4 directions from here
            found = dfs(r - 1, c, index + 1) or dfs(r + 1, c, index + 1) or dfs(r, c - 1, index + 1) or dfs(r, c + 1, index + 1)

            board[r][c] = temp # Put the value back
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True 
    
        return False