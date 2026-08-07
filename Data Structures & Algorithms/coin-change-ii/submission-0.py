class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # For each amount, we want to know how many ways we can make up the amount
        dp_arr = [0 for _ in range(amount + 1)]
        dp_arr[0] = 1

        for coin in coins:
            # We iterate through each coin first
            # print("We are checking with the $", coin)
            for curr_amt in range(1, amount + 1):
                # We want to see how many ways can we make up this amount using this coin
                remaining = curr_amt - coin
                # print("remaining amount if we used the $", coin, "coin =", remaining)
                if remaining >= 0:
                    dp_arr[curr_amt] = dp_arr[curr_amt] + dp_arr[remaining]
                    # print("number of ways to get", curr_amt, "is", dp_arr[curr_amt])
        
        return dp_arr[amount]