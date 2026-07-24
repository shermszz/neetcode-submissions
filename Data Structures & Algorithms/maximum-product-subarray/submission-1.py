class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # An array of size 1 is itself the maxProduct, this is the base case
        
        if len(nums) == 1:
            return nums[0]
        
        max_product_so_far = nums[0]
        curr_max, curr_min = nums[0], nums[0]
        print("initial max is =", max_product_so_far)

        for i in range(1, len(nums)):
            # Currently standing on nums[i], we have 2 options:

            # 1. Take this value, multiply with the previous maximal value
            # We should also take this value, and see what we get with the minimal value in case 2 negatives make an even larger positive value
            take_val_max = nums[i] * curr_max
            take_val_min = nums[i] * curr_min
            print("If i take the value we are on, and multiply with my previous max, my new value is", take_val_max)
            print("If i take the value we are on, and multiply with my previous min, my new value is", take_val_min)

            # 2. We don't take this value, so our new subarray will have to shift to this position itself
            dont_take = nums[i]
            print("If i choose not to take it, my new maximum will be", dont_take)

            # Now, we compare and see which one yields a better value
            curr_max = max(take_val_min, take_val_max, dont_take)
            curr_min = min(take_val_min, take_val_max, dont_take)
            print("Current_max =", curr_max)
            print("Current_min =", curr_min)
            max_product_so_far = max(max_product_so_far, curr_max)
            print("My updated max is =", max_product_so_far)
        
        return max_product_so_far

"""
=========================================================
KEY LEARNINGS: Maximum Product Subarray (LeetCode 152)
=========================================================

CORE CONCEPTS:
1. Kadane's Extension: To find the max contiguous subarray, at each 
   step you decide to either extend the previous subarray or start a 
   new one right here.
2. The Double Negative Pivot: In multiplication, the lowest possible 
   negative number is just one negative multiplier away from becoming 
   the highest possible positive number.
3. The 3-Way Bucket: Because signs flip, you cannot pre-determine if 
   multiplying by the previous max or min will yield the best result. 
   Evaluate (num * max), (num * min), and (num alone), and pick the 
   absolute highest and lowest of those three to carry forward.

GUIDING HINTS & TRAPS AVOIDED:
- The Mediocrity Rule: You do not need to track all inner subarrays. 
  A subarray that is neither the maximum nor the minimum at `i-1` has 
  zero mathematical chance of becoming the maximum at `i`.
=========================================================
"""