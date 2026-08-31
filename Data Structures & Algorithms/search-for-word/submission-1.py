class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """ 
        For this question, we have an index to check each letter in the word
        We have a dfs helper function to track the index of the word and the directions we can go to are NSEW

        """
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        rows, cols = len(board), len(board[0])
        index = 0 # Pointer at the word
        
        def dfs(row: int, col: int, index: int) -> bool:
            # 1. check for success first
            if index == len(word):
                # If we managed to find all letters of the word, then we have found it 
                return True
            
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            
            if board[row][col] != word[index]:
                return False
            
            temp = board[row][col]
            board[row][col] = "#"
            found = dfs(row - 1, col, index + 1) or dfs(row, col - 1 , index + 1) or dfs(row + 1, col, index + 1) or dfs(row, col + 1, index + 1)

            board[row][col] = temp
            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] != word[index]:
                    continue 
                # Otherwise if we find a match, we should dig deeper into it
                if dfs(i, j, index):
                    return True
        return False