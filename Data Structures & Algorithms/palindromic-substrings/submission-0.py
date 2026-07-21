class Solution:
    def countSubstrings(self, s: str) -> int:
        # Every individual letter inside the string is a palindrome

        # We need information of the first letter of a substring and the second letter of a substring
        # To do this, we need a 2D array to track for every possible position, if that combination of [first, second] is a valid palindrome or not

        # Build this using bottom up approach, starting with length 2 all the way up to len(s)

        n = len(s)
        dp_grid = [[False for _ in range(n)] for _ in range(n)]
        total_count = 0

        # 1. Base case, all strings of length 1 are palindromes, which is added to the overall count
        for i in range(n):
            dp_grid[i][i] = True
            total_count += 1
        
        # Starting from length 2 onwards up till the full length of the string
        for length in range(2, n + 1):
            # Then, for all valid starting points of each substring
            for start in range(n - length + 1):
                end = start + length - 1 # Compute a valid end pooint of the substring
                if s[start] == s[end]:
                    # Edge case for a valid palindrome of size length 2, since there is no need to check in between them
                    if length == 2 or dp_grid[start + 1][end - 1]:
                        dp_grid[start][end] = True
                        total_count += 1
                
        return total_count

"""
=========================================================
KEY LEARNINGS: Palindromic Substrings (LeetCode 647)
=========================================================

CORE CONCEPTS:
1. Pattern Recognition: This is the exact same underlying mechanism as 
   Longest Palindromic Substring. Once you learn the 2D DP grid structure 
   for intervals (start, end), you can apply it to counting, finding the 
   longest, or checking validity.
2. The Clean Transition: Consolidating your logic into a single check 
   `if s[i] == s[j] and (length == 2 or dp[i+1][j-1])` prevents nasty 
   bugs where conditions accidentally overlap.

GUIDING HINTS & TRAPS AVOIDED:
- The Double-Count Trap: Using independent `if` statements instead of 
  `elif` or an `or` clause can cause overlapping conditions to fire twice.
- Space Optimization: DP is $O(N^2)$ space. If an interviewer demands 
  $O(1)$ space for palindrome problems, pivot away from DP and use the 
  "Expand Around Center" two-pointer technique.
=========================================================
"""