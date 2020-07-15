class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 动态规划
        # 利用prices数组的空间，prices[i]记录i及之前的数组值中最小的那个
        # 时间复杂度O(n)，空间复杂度O(1)
        res = 0
        for i in range(1, len(prices)):
            res = max(res, prices[i] - prices[i-1])
            prices[i] = min(prices[i-1], prices[i])
        return res