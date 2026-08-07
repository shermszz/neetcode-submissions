class Solution {
    public int coinChange(int[] coins, int amount) {
        // For this question, we want to maintain a dp array to tell us that at each amount value, what is the fewest number of coins required to make up that amount
        int[] dp_arr = new int[amount + 1];
        // At each index of dp_arr, we want to be able to know what is the fewest number of coins needed to make up the amount represented by the index

        dp_arr[0] = 0; // Base case, we need 0 coins to make up $0

        for (int i = 1; i < amount + 1; i++) {
            // Loop thorugh each coin inside coins, and find the minimum coins if possible
            int minimum_required = amount + 1;
            for (int coin : coins) {
                // If i took ${coin}, whats the remaining amount?
                int remaining = i - coin;
                if (remaining >= 0 && dp_arr[remaining] != -1) {
                    // Then we check what the feweest number of coins requried to make up the minimum and compare that with what we need now
                    minimum_required = Math.min(minimum_required, dp_arr[remaining] + 1);
                }
            }
            if (minimum_required == amount + 1) {
                minimum_required = -1;
            }
            dp_arr[i] = minimum_required;
        }
        return dp_arr[amount];
    }
}
