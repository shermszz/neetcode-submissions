class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Everytime you pay the cost[i], you can choose to take to the i + 1 or i + 2 floor.
        # We are given the option to start either at cost[0] or cost[1]
            # We could greedily start at the cheaper staircase first.
            # OR we could simulate for every step that we take
        
        min_cost, n = 0, len(cost)

        # We can spawn at either index 0 or 1, so cost = 0
        cost_two_steps_back = 0 # cost to reach step 0, which is free
        cost_one_step_back = 0 # cost to reach step 1, which is free

        for i in range(2, n + 1):
            # We need to find the minimum cost to reach staircase i
            min_cost = min(cost_two_steps_back + cost[i - 2], cost_one_step_back + cost[i - 1])

            # Now that we have the minimum cost to reach staircase i, we update the previous two counts
            cost_two_steps_back, cost_one_step_back = cost_one_step_back, min_cost
            # This updates cost to reach step[i - 1] and cost to reach step[i]
            # This update is the minimum possible cost, which is why we can keep moving forward like this
        
        return min_cost

"""
=========================================================
KEY LEARNINGS: Min Cost Climbing Stairs (LeetCode 746)
=========================================================

CORE CONCEPTS:
1. The Backward-Looking DP Mindset: Instead of standing on a step and 
   calculating forward to see where you can go, stand on the destination 
   step and look backward to see the cheapest way to arrive. 
2. The Definition of "The Top": Reaching the top of the stairs means 
   reaching one index PAST the end of the array (index `n`). It is okay 
   if a 2-step jump technically overshoots the final index.
3. State Representation: The values stored in our DP variables track the 
   minimum cost to REACH a step, not the cost to LEAVE it. 

GUIDING HINTS & TRAPS AVOIDED:
- The Entry Fee Trap: You can start at index 0 or index 1 for free. 
  You only pay the `cost[i]` when you JUMP from that step. This is why 
  our two sticky notes both start at 0.
- The Forward Simulation Trap: Trying to simulate all possible paths 
  forward results in an O(2^n) exponential explosion. Always build from 
  the base cases upward.
=========================================================
"""