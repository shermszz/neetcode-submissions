class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        # With this array, for every amount, we want to check all the coins we have, how many can be used to make up this amount, what is the fewest possible number of coins
        for curr_amt in range(1, amount + 1):
            # What is the minimum number of coins I need to make up this curr_amount?
            for coin_amt in coins:
                # print("After using this coin, I am left with value", curr_amt - coin_amt)
                if curr_amt - coin_amt >= 0:
                    dp[curr_amt] = min(dp[curr_amt], 1 + dp[curr_amt - coin_amt])
        return dp[amount] if dp[amount] != float('inf') else -1