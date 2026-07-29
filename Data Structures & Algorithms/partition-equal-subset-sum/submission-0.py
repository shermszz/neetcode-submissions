class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # One important observation is that each subset sum must be exactly total_sum / 2
        total_sum = sum(nums)
        print("total sum of the array is", total_sum)

        if total_sum % 2 != 0:
            # An array with odd sum can never have 2 subsets of the same value
            return False

        # Now, we are dealing with a case where total sum is even
        running_sum = 0
        target = total_sum // 2

        # Create a dp set. 
        # Inside this set, we store the sums that we are able to form with the numbers we have seen so far
        dp_set = set()
        dp_set.add(0) # We start with 0, since to get a sum of 0, we need 0 numbers, so by default it is true
        
        for i in range(len(nums)):
            # Generate new sums using set comprehension
            # merge them into the existing dp_set using update()
            dp_set.update({num + nums[i] for num in dp_set}) # Short hand for the follow code below
            """ 
            new_values = []
            for num in dp_set:
                new_val = num + nums[i]
                new_values.append(new_val)
            for num in new_values:
                dp_set.add(num)
            """
            if target in dp_set:
                return True
        return False

"""
=========================================================
KEY LEARNINGS: Partition Equal Subset Sum (LeetCode 416)
=========================================================

CORE CONCEPTS:
1. The 0/1 Knapsack Paradigm Shift: When a problem asks you to "pick 
   or not pick" numbers to reach a target, stop tracking array indices. 
   Instead, track the reachable SUMS. 
2. The "Bucket of Sums" (Set Optimization): Instead of a massive 
   boolean array of size `target` (where you waste time looping over 
   `False` values), use a HashSet. For every new number, add it to 
   every sum currently in your set.
3. Pseudo-Polynomial Time: $O(N * target)$ sounds slow, but it collapses 
   trillions of redundant branches (O(2^N)) into a single pass. It is 
   a massive Time-Space Tradeoff victory.

GUIDING HINTS & TRAPS AVOIDED:
- The Odd Sum Exit: Always check `if sum(nums) % 2 != 0` first. You 
  cannot evenly split an odd number.
- The Concurrent Modification Trap: You cannot add items to a set 
  while you are looping through it (Python will crash). You must create 
  the new sums first, then merge them in.
- The Float Trap: `total_sum / 2` creates a float (e.g., 5.0). Always 
  use integer division `total_sum // 2` for targets.
- The Pythonic 1-Liner: 
  `dp_set.update({num + curr_val for num in dp_set})` handles the loop, 
  the temporary creation, and the merging in highly optimized C-code.
=========================================================
"""