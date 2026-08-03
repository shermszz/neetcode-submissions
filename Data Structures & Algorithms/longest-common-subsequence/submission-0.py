class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # For the shorter string, we try to see what is the longest common subsequence

        # We need a 2D dp grid.
        # If you only look at the first i characters in shorter string and the first j characters of the longer string, dp[i][j] should tell us the longest common subsequence so far
        n, m = len(text1), len(text2) # n columns, m rows
        dp_grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # We must +1 for each row and column to denote that region as the "empty string" region
        
        # print("Initial grid", dp_grid)

        for i in range(1, m + 1):
            first_char = text2[i - 1]
            for j in range(1, n + 1):
                curr_char = text1[j - 1]
                # print("comparing", first_char, curr_char)
                if first_char == curr_char:
                    # if we found a match, that means the character could contribute to the longest common subsequence
                    # what we do is add to the longest sequence of either text that didnt have this letter yet
                    # this happens to be diagnonally up and left to where we are now
                    dp_grid[i][j] = dp_grid[i - 1][j - 1] + 1
                    # print(dp_grid[i][j])
                else:
                    # If they do not match, one of the characters could be useless
                    # Hence, we should consider the case where we don't take the character from text1, or if we don't take the character from text2
                    throw_away_first_char = dp_grid[i - 1][j]
                    throw_away_curr_char = dp_grid[i][j - 1]
                    dp_grid[i][j] = max(throw_away_first_char, throw_away_curr_char)

        return dp_grid[m][n]