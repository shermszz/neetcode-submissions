# This solution is the BOTTOM-UP Dynamic Programming approach 
# Uses O(N) time and O(1) space
class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. Handle the base cases immediately. 
        # If n is 1 or 2, the answer is just n!
        if n <= 2:
            return n
        
        # 2. Setup our two "sticky notes" for Step 1 and Step 2
        two_steps_back = 1
        one_step_back = 2

        # 3. Start climbing from step 3 up to N
        for i in range(3, n + 1):
            # Current number of ways to climb i steps
            current = two_steps_back + one_step_back
            print("num distinct ways to climb", i, "steps:",current)

            two_steps_back = one_step_back
            one_step_back = current

        return one_step_back


"""
=========================================================
KEY LEARNINGS: Climbing Stairs (LeetCode 70)
=========================================================

CORE CONCEPTS:
1. The Overlapping Subproblem: Naive recursion recalculates the same 
   branches over and over, leading to O(2^n) time complexity. 
2. Top-Down DP (Memoization): Keep the recursive structure, but add a 
   Dictionary (Cache). 
   - GUARD: Check if `n` is in cache before doing math.
   - SAVE: Save the result to cache before returning.
   - Space Complexity: O(N) due to the dictionary and Call Stack.
3. Bottom-Up DP (Tabulation / Sliding Window): Flip the problem. Start 
   from the base cases and use a loop to build forward. Because we only 
   ever need the previous two answers, we only need two variables instead 
   of a full array.
   - Space Complexity: O(1) Constant Space.

GUIDING HINTS & TRAPS AVOIDED:
- The Base Case Loop Trap: Never put `if i == 1:` base cases inside 
  your DP loop. Handle them at the very top of the function (`if n <= 2:`), 
  then initialize your variables, then start your loop at 3.
- Variable Naming: Avoid `first` and `second` as they get confusing 
  when moving forward. Use `one_step_back` and `two_steps_back`.
=========================================================
"""