class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # At any position in the array, we have a value curr = nums[i]
        # We want to know for each position 0 to i - 1, what was the longest increasing subsequence, and whether this current value can add to this longest running sequence?

        n = len(nums)
        dp_arr = [1 for i in range(n)] # Each slot represnets the length of the longest subsequence that ends at index i

        for i in range(1, n):
            # print("New iteration, end point is index", i)
            curr = nums[i]
            # print("curr value now = ", curr)
            for j in range(i):
                # I want to first know what is the longest subsequence of the element just before me
                curr_longest = dp_arr[j]
                # print("curr_longest subsequence at index", j, "is", curr_longest)

                # Then, I want to know what are the previous values, iterating through one at a time
                prev = nums[j]
                # print("prev val at index", j, "=", prev)

                # Check if my curr value can extend the any of the previous values from 0 to i - 1
                if curr > prev:
                    # This means that on our current value standing, we have found 1 more increasing subsequence
                    # So we update our dp array
                    # print("curr value is bigger than prev, updating dp_arr at index", i)
                    dp_arr[i] = max(dp_arr[i], dp_arr[j] + 1)
                    # print("dp_arr state is", dp_arr)

        return max(dp_arr)

"""
=========================================================
KEY LEARNINGS: Longest Increasing Subsequence (LeetCode 300)
=========================================================

CORE CONCEPTS:
1. The 1D "Look-Back" Pattern: dp[i] represents the longest sequence 
   that STRICTLY ENDS at index i.
2. Initialization: Unlike sums (where base is 0), the minimum length 
   of any subsequence is 1 (the number itself). Initialize the DP 
   array with 1s.
3. The Relay Race: For every number i, look at all previous numbers j. 
   If nums[i] > nums[j], it's a legal pass. Your new score becomes 
   max(current_score, score_at_j + 1).

GUIDING HINTS & TRAPS AVOIDED:
- The Accumulation Trap: Do not just do `dp[i] += 1`. You are looking 
  for the SINGLE longest path to connect to, not counting all of them.
- The Final Answer Trap: The longest sequence in the array might not 
  end at the very last number. You must return `max(dp_arr)`, not 
  `dp_arr[-1]`.
=========================================================
"""