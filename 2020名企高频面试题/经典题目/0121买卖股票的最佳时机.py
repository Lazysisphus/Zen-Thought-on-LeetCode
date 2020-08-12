class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp：转换为求连续子数组最大和问题
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        for i in range(n - 1):
            prices[i] = prices[i + 1] - prices[i]
        prices = prices[: -1]

        m = len(prices)
        for i in range(1, m):
            prices[i] = max(prices[i - 1] + prices[i], prices[i])
        return max(max(prices), 0)

        # dp，不转换问题
        n = len(prices)
        if n == 0 or n == 1: 
            return 0
        dp = [0 for _ in range(n)]
        minprice = prices[0] 
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)
        return dp[-1]