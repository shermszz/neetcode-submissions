class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Since we can use the words an unlimited number of times, this is unbounded knapsack
        
        # First, convert the wordDict into a set for O(1) lookup
        word_set = set(wordDict)
        n = len(s)

        # Each dp[i] tells us if the string s[0: i] can be formed by ANY of the words in wordDict
        # If it can, then we set its value to be True
        dp_arr = [False for _ in range(n + 1)]
        dp_arr[0] = True # Set this to true first

        for i in range(1, n + 1):
            # print("Index i =", i)
            for j in range(i):
                # We want to check if the substring from 0 to j is in the dictionary or not
                # Since we are doing bottom up, we can just check dp_arr[j] if the left substring is part of wordDict already or not
                left = dp_arr[j] # Did the left piece (0 to j) form a valid chain of words?
                
                right = s[j : i] # Is the right piece (j to i) a valid word in the dictionary?
                # print("Left value is", left)
                # print("Right side substring is", right)
                if left and right in word_set:
                    # If the left chain is unbroken and the right piece is a word inside wordDict
                    # Then we know that index i is a safe checkpoint for future reference.
                    dp_arr[i] = True

                    # We only need ONE valid way to reach i, so we can stop checking j's
                    break
            # print(dp_arr)
        return dp_arr[n]

"""
=========================================================
KEY LEARNINGS: Word Break (LeetCode 139)
=========================================================

CORE CONCEPTS:
1. The Checkpoint Concept (1D DP): dp[i] does not mean "is this 
   substring exactly one word". It means "is index `i` a valid 
   stopping point that can be built using ANY combination of words 
   from the start of the string?"
2. The "Knife" Strategy: You need two loops. The outer loop `i` marks 
   the end of the current substring. The inner loop `j` acts as a knife, 
   sweeping across and cutting the string into a left half and a right half.
3. Don't Recalculate the Past: Never check if the left half is in the 
   dictionary. You already did that work! Just look at `dp[j]` to see 
   if it was a valid checkpoint.

GUIDING HINTS & TRAPS AVOIDED:
- The Greedy Trap: You cannot just lock in the first word you find 
  reading left-to-right, because words can overlap (e.g., "cat" vs "cats"). 
  You must check all previous `j` breakpoints.
- Early Exit: As soon as you find ONE valid way to bridge the gap and 
  make `dp[i] = True`, `break` the inner loop. You only need to know 
  it's possible, not how many ways it's possible.
- O(1) Dictionary: Always convert a list of words into a `set` before 
  looping so lookups take O(1) instead of O(W).
=========================================================
"""
