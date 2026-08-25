class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Trying a backtracking solution, but now with memoization

        # Each number in nums can either be +ve or -ve. 
        # So, we try every possible subset sum and check if each sum we have found is equal to the target value
        n = len(nums)
        memo = {} # To store (index, curr_sum) -> number of ways to reach the final target with the remaining numbers 
        def backtrack(index: int, curr_sum: int) -> int:
            # 1. We first check our memo table to see whether the number of ways is already recorded
            if memo.get((index, curr_sum)) is not None:
                return memo[(index, curr_sum)]
            
            # 2. We do a base case check 
            if index == n:
                if curr_sum == target:
                    memo[(index, curr_sum)] = 1
                    return 1
                return 0
            
            curr_num = nums[index]
            memo[(index, curr_sum)] = backtrack(index + 1, curr_sum + curr_num) + backtrack(index + 1, curr_sum - curr_num)
            return memo[(index, curr_sum)]
            
        return backtrack(0, 0)

"""
=========================================================
KEY LEARNINGS: Target Sum (LeetCode 494) - Top-Down DP
=========================================================

CORE CONCEPTS:
1. Identifying the "State": In DP, the state is the set of variables that 
   uniquely define your current position. Here, the remaining numbers you 
   can use are determined by your `index`, and your progress is determined 
   by your `curr_sum`. Therefore, the cache key must be `(index, curr_sum)`.
2. Returning vs. Tallying: To use a cache, a recursive function must 
   return an answer to its parent, rather than updating a global variable. 
   The parent relies on the children's returned answers to calculate its 
   own answer.
3. The 2D Top-Down Advantage: Top-Down DP (Recursion + Dictionary) is 
   highly preferred over Bottom-Up (2D Array) for this problem because 
   `curr_sum` can be negative. Dictionaries handle negative keys perfectly, 
   whereas 2D arrays would require messy index-shifting math to avoid 
   negative array indices.
=========================================================
"""
