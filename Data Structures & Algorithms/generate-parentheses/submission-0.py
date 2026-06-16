class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open_count, close_count, curr_string):
            if len(curr_string) == 2 * n:
                # The string that is created is a well-formed parentheses
                res.append(curr_string)
                return
            if open_count < n:
                backtrack(open_count + 1, close_count, curr_string + "(")
            if close_count < open_count:
                backtrack(open_count, close_count + 1, curr_string + ")")
        backtrack(0, 0, "")
        return res

"""
=========================================================
KEY LEARNINGS: Generate Parentheses (LeetCode 22)
=========================================================

CORE CONCEPTS:
1. Slot-Based Choices: Shift your mental model from "Include/Exclude 
   an item" to "Which valid option can I place in this next slot?"
2. The Two Bouncers: 
   - Open Bracket Rule: Can only add if `open_count < n`.
   - Close Bracket Rule: Can only add if `close_count < open_count`.
3. String Immutability (The Ghost Bucket): Because strings in Python 
   cannot be modified in place, passing `curr_string + "("` creates a 
   temporary copy for that specific recursive branch. 
   - This means you DO NOT need to `.pop()`! 
   - When a branch finishes, the parent node's string is perfectly 
     untouched and ready to evaluate the next `if` statement.

GUIDING HINTS & TRAPS AVOIDED:
- Base Case Math: If your problem requires `n` pairs, a completed 
  sequence will always have a length of `2 * n`.
- Variable Modification Trap: Never do `curr_string += "X"` before a 
  recursive call if you have multiple choices at the same level. Pass 
  the addition directly inside the function arguments to avoid 
  polluting the variables for the next `if` statement!
=========================================================
"""