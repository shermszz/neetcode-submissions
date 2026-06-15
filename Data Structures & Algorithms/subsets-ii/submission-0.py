class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Since there are duplicates now, when we are excluding elements, we need to fast forward and remove all elements that are the same as the one we just included
        # To do this efficiently, we first sort the array nums
        nums.sort()
        res, n = [], len(nums)

        def backtrack(index: int, bucket: List[int]) -> None:
            if index == n:
                res.append(bucket.copy())
                return

            # 1. INCLUDE step
            curr = nums[index]
            bucket.append(curr)
            backtrack(index + 1, bucket)

            # 2. EXCLUDE step
            bucket.pop()
            # To properly exclude any duplicates, we keep fast forwarding until we meet a differnet number
            while index < n and nums[index] == curr:
                index += 1
            backtrack(index, bucket)
        backtrack(0, [])
        return res

"""
=========================================================
KEY LEARNINGS: Subsets II (LeetCode 90)
=========================================================

CORE CONCEPTS:
1. Pattern Recognition: If a problem asks for combinations or subsets 
   AND the input array contains duplicates, you immediately know you 
   need the "Sort + Fast-Forward Exclude" pattern.
2. Pruning vs. Filtering: Pruning (skipping duplicate branches during 
   recursion) is infinitely better than Filtering (generating everything 
   and using a Set to remove duplicates at the end). Pruning saves Time; 
   Filtering only saves the final Output.

GUIDING HINTS & TRAPS AVOIDED:
- The Exclude Tracker: When doing the fast-forward skip in a Subsets 
  problem, grab the value of `curr = nums[index]` during the Include step. 
  That way, during the Exclude step, you have a static reference of exactly 
  which value you are trying to skip!
=========================================================
"""