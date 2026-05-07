class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minArr, n = [], len(prices)
        currMin = float('inf')
        for i in range(n):
            if prices[i] < currMin:
                currMin = prices[i]
            minArr.append(currMin)
        print(minArr) # If sold on day i, minArr[i] tells us the lowest price that could have been bought earlier

        max_profit = 0
        for i in range(n):
            # If sell on day i, I buy at minArr[i]
            profit = prices[i] - minArr[i]
            max_profit = max(profit, max_profit)

        return max_profit