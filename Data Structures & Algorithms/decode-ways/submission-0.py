class Solution:
    def numDecodings(self, s: str) -> int:    
        n = len(s)
        count = 0
        
        two_steps_back = 1 # Trivially true
        one_step_back = 1 if int(s[0]) != 0 else 0

        for i in range(1, n):
            curr_ways = 0
        
            # 1. First, we choose to use only the current single digit
            curr_one_digit = int(s[i])
            # We just want to check, is this single digit valid on its own. 
            # If so, that means we can append this valid digit with all other valid string of numbers before this single digit
            if curr_one_digit != 0:
                # Then this single digit by itself is valid
                curr_ways += one_step_back
            
            # 2. We try using 2 digits now
            curr_two_digit = int(s[i - 1: i + 1])
            if 10 <= curr_two_digit <= 26:
                # Then this 2 digit is also valid
                # This means we can convert this 2 digit into a letter, and append this letter to all other valid letters formed by all the digits before these 2 digits
                curr_ways += two_steps_back
            
            two_steps_back, one_step_back = one_step_back, curr_ways
        return one_step_back

"""
=========================================================
KEY LEARNINGS: Decode Ways (LeetCode 91)
=========================================================

CORE CONCEPTS:
1. Climbing Stairs in Disguise: Finding the number of ways to group 
   items in sizes of 1 or 2 is mechanically identical to climbing stairs 
   1 or 2 steps at a time.
2. The "Box of Strings" Accumulation: When a move is valid, you do not 
   add +1 to your count. You carry forward the entire historical count of 
   valid paths that existed before that move. 
   - A valid 1-jump inherits the paths from 1 step back.
   - A valid 2-jump inherits the paths from 2 steps back.

GUIDING HINTS & TRAPS AVOIDED:
- The Zero Trap: Unlike stairways, strings can have invalid states 
  (the number '0', or two digits > 26). You must conditionally check 
  validity before adding a historical count. 
- Space Optimization: Because you only ever look back `i-1` and `i-2`, 
  you do not need a DP array. Two variables updated dynamically provide 
  an O(1) space solution.
=========================================================
"""