class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, n = [], len(nums)

        def backtrack(curr_index: int, curr_sum: int, bucket: List[int]) -> None:
            # 1. Base case: When curr_index has reached the end of the list
            if curr_index == n or curr_sum >= target:
                if curr_sum == target:
                    res.append(bucket.copy())
                return
            # 2. Otherwise, we try to include the next number 
            next_num = nums[curr_index]
            bucket.append(next_num)
            # Do not increment curr_index, since we can include the number any number of times
            backtrack(curr_index, curr_sum + next_num, bucket)

            # 3. Then, we exclude the number and carry on
            bucket.pop()
            backtrack(curr_index + 1, curr_sum, bucket)
        
        backtrack(0, 0, [])
        return res

"""
=========================================================
KEY LEARNINGS: Combination Sum (LeetCode 39)
=========================================================

CORE CONCEPTS:
1. Unlimited Choices (The "Stay Here" Trick): When a problem allows 
   you to reuse the same element an unlimited number of times, your 
   "Include" recursive call should NOT increment the index. 
   -> `backtrack(curr_index, ...)` instead of `curr_index + 1`.
2. The "Ghost Bucket" Tracker: Never wait until the end of a branch 
   to validate a sum if the branch can grow infinitely. Pass a 
   `curr_sum` (or `remaining_target`) down the tree to check your 
   status at every single step.

GUIDING HINTS & TRAPS AVOIDED:
- Base Case Hierarchy: Always check your "Bust" condition 
  (`curr_sum > target`) and your "Success" condition (`curr_sum == target`) 
  BEFORE you do your include/exclude logic to prevent infinite recursion.
- The Exclude Step: Even though the Include step stays on the same index, 
  the Exclude step MUST move forward (`curr_index + 1`). Otherwise, you 
  will just infinitely evaluate the exact same state.
=========================================================
"""