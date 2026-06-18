class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        start, end = 0, len(s)

        def is_palindrome(s):
            palindrome = True
            left, right = 0, len(s) - 1
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    palindrome = False
                    break
            return palindrome
        
        def backtrack(index, bucket):
            if index == len(s): # Hit the end of the string already
                res.append(bucket.copy()) # Save the result
                return

            # Initialize a for loop to check every possible substring
            for i in range(index, end):
                curr_str = s[index : i + 1]
                if is_palindrome(curr_str):
                    bucket.append(curr_str)
                    backtrack(i + 1, bucket) # Recurse only if the curr_str is indeed a palindrome
                    bucket.pop()
        backtrack(0, [])
        return res

"""
=========================================================
KEY LEARNINGS: Palindrome Partitioning (LeetCode 131)
=========================================================

CORE CONCEPTS:
1. The Chopping Block: When a problem asks you to partition or split 
   a string, your `for` loop determines "where to put the knife."
   - The loop range is `for i in range(start_index, len(s))`
   - The current slice is `s[start_index : i + 1]`
2. The Overlapping Knife Trap: If you just cut a slice that ends at 
   index `i`, the leftovers begin at `i + 1`. NEVER pass `index + 1` 
   into the recursive call, or your next cut will slice backwards into 
   the piece you just removed!
3. The Bouncer: You must validate the choice BEFORE making the 
   recursive call. 
   - `if is_valid(slice):`
   -     `bucket.append(slice)`
   -     `backtrack(i + 1, bucket)`
   -     `bucket.pop()`

GUIDING HINTS & TRAPS AVOIDED:
- Starting State: Always ensure your initial `bucket` is an empty 
  list `[]`, not your final `res` array.
- Function Placement: Helper functions like `is_palindrome` should be 
  placed OUTSIDE the recursive function so Python doesn't waste memory 
  destroying and recreating the function thousands of times.
=========================================================
"""

