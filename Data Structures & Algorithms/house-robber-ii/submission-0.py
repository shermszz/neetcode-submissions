class Solution:
    def rob(self, nums: List[int]) -> int:
        # Similar to House Robber 1, but now instead of a straight line, the houses are in a circle
        # THE TRICK: Since it is a circle, we cannot rob house 0 and house N - 1 together
            # So, what if in one scenario, we rob houses 1 to N - 1
            # in another scenario, we rob houses 0 to N - 2
            # Then, each scenario runs the normal House Robber 1 Logic
            # Then we find the max of the two and return it
        n = len(nums)

        if n == 1:
            # Edge case scenario
            return nums[0]

        def rob_normally(start: int, end: int, nums: list[int]) -> int:
            # Track the max profit AND index of the house we are at
            two_houses_back = 0
            one_house_back = 0

            for i in range(start, end):
                # We are at the house[i], we need to check if worth to rob or not. 
                curr_house_cash = nums[i]
                
                # 1. We choose to rob right now
                rob_now = two_houses_back + curr_house_cash

                # 2. We choose to rob later
                rob_later = one_house_back

                # 3. Find the maximum of the 2 to maximise your profits
                curr_max = max(rob_now, rob_later)

                two_houses_back, one_house_back = one_house_back, curr_max

            return one_house_back

        return max(rob_normally(0, n - 1, nums), rob_normally(1, n, nums))

"""
=========================================================
KEY LEARNINGS: House Robber II (LeetCode 213)
=========================================================

CORE CONCEPTS:
1. The Circular Trap: If elements are in a circle, the first and last 
   elements are neighbors and cannot be picked together. 
2. Splitting the Universe: Instead of writing complex conditional logic 
   to track the first house, split the problem into two linear sub-problems:
   - Reality A: Ignore the last house (indices 0 to N-2)
   - Reality B: Ignore the first house (indices 1 to N-1)
3. Return the maximum of these two realities.

GUIDING HINTS & TRAPS AVOIDED:
- The Slicing Trap: Do not pass `nums[1:]` into your helper function. 
  Slicing creates a new array in Python, destroying your O(1) space 
  complexity. Pass boundary indices (`start`, `end`) instead.
- The 1-Element Edge Case: If the array only has 1 element, splitting it 
  into two realities results in empty arrays. Always guard against 
  `len(nums) == 1` at the very top!
=========================================================
"""