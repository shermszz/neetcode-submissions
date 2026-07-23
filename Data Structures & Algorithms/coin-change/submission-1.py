class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # We start with a bottom up approach, considering that if amount is 0, we need 0 coins

        n = len(coins)
        dp_arr = [float('inf') for _ in range(amount + 1)]

        dp_arr[0] = 0 # Since to make up 0 dollars, we need 0 coins. This is our Base case
        for curr in range(1, amount + 1):
            # For each amount curr, we find out how many valid number of coins there are to make up the curr amount
            for val in coins:
                if val > curr:
                    # The coin value is bigger than the amount, so we skip it
                    continue
                # 1. Say we choose to take the coin now
                # take_coin would thus be 1 + (minimum number of coins to get curr - i amount)
                take_coin = dp_arr[curr - val] + 1

                # 2. If we choose not to take any coins, we are left with the minimum number of coins dp_arr[curr] currently holds
                dont_take_coin = dp_arr[curr]

                # Now, we make the decision, and we choose the minium
                dp_arr[curr] = min(take_coin, dont_take_coin)
        return dp_arr[amount] if dp_arr[amount] != float('inf') else -1

"""
=========================================================
KEY LEARNINGS: Coin Change (LeetCode 322)
=========================================================

CORE CONCEPTS:
1. Unbounded Knapsack (1D DP): When you have an infinite supply of 
   items (coins) to reach a target (amount), the state is defined 
   solely by the target. This makes it a 1D DP problem, not 2D.
2. Initialization for Minimums: When searching for a minimum value, 
   always initialize your DP array with `float('inf')` (Infinity). 
   Your base case `dp[0] = 0` provides the starting anchor.
3. The Nested Choice: For every target amount, you iterate through 
   every coin and ask: "Is 1 + (minimum coins needed for the remainder) 
   better than my current known best?"

GUIDING HINTS & TRAPS AVOIDED:
- The Array Size Trap: An array tracking amounts from 0 to `N` needs 
  `N + 1` slots. Always initialize with `amount + 1` and loop to `amount + 1`.
- The Value vs. Index Trap: Iterate through the items themselves 
  (`for coin in coins`) rather than their indices to avoid accidentally 
  doing math with the index instead of the monetary value.
- The Impossible State Check: If the final answer remains `inf`, it 
  means the target cannot be reached by any combination. Return `-1`.
=========================================================
"""