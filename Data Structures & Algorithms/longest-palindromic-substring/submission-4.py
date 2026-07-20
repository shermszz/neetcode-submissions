class Solution:
    def longestPalindrome(self, s: str) -> str:
        # This is a 2D DP problem because we need to keep track of 2 things:
        # i (start of substring), and j (end of substring)
        # We check if s[i] == s[j] AND the words in between them are a palindrome. 
        # So we work our way bottom up from the base cases
        n = len(s)
        dp_grid = [[False for _ in range(n)] for _ in range(n)]

        # Edge case: If s contains a single letter OR s is a string of distinct letters
        # We need to return just the single letter  
        longest = s[0]

        # 1. Base case: The diagonals along the matrix are going to be palindromes
        for i in range(n):
            dp_grid[i][i] = True
        
        # 2. For every other substring, we loop by the length of the substring
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # For every other string that is more than length 1
                if s[i] == s[j]:
                    # print("The letter", s[i], "matches at indices i =", i, "and j =", j)
                    # Check if within the grid, they are palindromes or trivially true
                    if i + 1 == j and j - 1 == i:
                        # This is a trivially true case, for when substring is of length 2
                        dp_grid[i][j] = True
                        longest = s[i : j + 1]
                    
                    elif dp_grid[i + 1][j - 1] is True:
                        dp_grid[i][j] = True
                        longest = s[i : j + 1]

        return longest