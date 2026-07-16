class Solution:
    def rob(self, nums: List[int]) -> int:
        # Cant just think about odd and even indices, the way you rob may not be in perfect order

        # We can start from index 0 OR index 1
        # From each step, we can take 2 or more steps afterwards. 
        max_profit = 0
        two_houses_back, one_house_back = 0, 0

        for i in range(len(nums)):
            # You are now at house[i], but you need to decide whether to ROB or NOT
            # 1. Check how much cash is in this house first
            curr_cash = nums[i]

            # 2. Now we check how much we can make if we rob this house
            # To rob this house, it means we could not have gotten the cash from the i - 1 house, it must have been the i - 2 house
            rob_now = two_houses_back + curr_cash
            
            # 3. We don't rob this house, then the profit we have now from one_house_back would become two_houses_back
            rob_later = one_house_back

            curr_max = max(rob_now, rob_later)
            
            # The house that we just stepped away from, we update to curr_max
            # This is because we always make the most optimal choice at every stop by doing the comparison of rob_now or rob_later
            two_houses_back, one_house_back = one_house_back, curr_max

        return one_house_back

"""
=========================================================
KEY LEARNINGS: House Robber (LeetCode 198)
=========================================================

CORE CONCEPTS:
1. State Definition: The variable `one_house_back` does NOT mean "the 
   money inside the last house." It means "the MAX total profit we could 
   possibly have right now, considering all houses up to the last one."
2. The Two Realities: At any given step, you only have two choices:
   - Rob it: `two_houses_back + current_cash`
   - Skip it: `one_house_back`
3. The Phantom Houses: Initializing your variables to 0 before the loop 
   acts like placing two "phantom" empty houses at the start of the street. 
   This perfectly prevents IndexError on arrays with only 1 or 2 items.

GUIDING HINTS & TRAPS AVOIDED:
- The Greedy Trap: Taking alternate houses (odd/even) fails. Always use 
  max() to let the math decide the optimal path.
- The Conditional Shift Trap: Never put your variable shift inside an 
  if/else block. Time always moves forward, so your variables must ALWAYS 
  shift forward unconditionally at the end of the loop.
=========================================================
"""