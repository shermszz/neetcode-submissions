class Solution:
    def longestPalindrome(self, s: str) -> str:
        # This is a 2D dp_grid that we need to use to keep track of how many palindromes there are
        n = len(s)
        dp_grid = [[False for _ in range(n)] for _ in range(n)]

        # First, we set every individual character to be true, since a single character is a palindrome
        for i in range(n):
            dp_grid[i][i] = True

        # Now, we need a double for loop to iterate through every substring possible and check if there is a longest substring 
        # For each substring, we want to check if the starting and ending characters are the same
        # If they are the same, check whether the characters in between them are a palindrome
        # If they are a palindrome, then we want to check the length, whether it is the longest seen so far. If it is the longest, we update our 2 pointers
        # at the end, we slice the string using the 2 pointers to return that palindromic string
        longest_left = 0
        longest_right = 0
        curr_longest = 0
        for i in range(n - 1, -1, -1):
            starting_char = s[i]
            # print("Current iteration", i,"has starting char", starting_char)
            for j in range(i + 1, n):
                curr_char = s[j]
                # print("current char is", curr_char)
                if starting_char != curr_char: 
                    # print("Characters do not match. Skipping...")
                    dp_grid[i][j] = False
                    continue
                # Edge case here, if the string is only 2 characters long
                if j - i == 1 or dp_grid[i + 1][j - 1]:
                    # print("Character match and is palindrome!")
                    dp_grid[i][j] = True
                    curr_length = j - i + 1
                    if curr_length > curr_longest:
                        curr_longest = curr_length
                        longest_left = i
                        longest_right = j
            # print("dp grid after iteration", i, "is", dp_grid)
        return s[longest_left : longest_right + 1]

