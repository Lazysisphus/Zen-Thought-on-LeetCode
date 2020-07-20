class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        # 动态规划
        # 令dp[n][s]表示掷完第n个骰子后和为s时，总共可能的排列数
        # 那么dp[n][s]=dp[n-1][s-1]+...+dp[n-1][s-6]
        # 0行、0列无实际意义，知识为了让索引对齐
        dp = [[0 for _ in range(n*6+1)] for _ in range(n+1)]
        # 初始化第1行，第1列到第6列
        for i in range(1, 7):
            dp[1][i] = 1
        for i in range(2, n+1):
            for j in range(i, i*6+1): # 遍历到第i行，和的范围是i~i*6
                for k in range(1, 7):
                    dp[i][j] += dp[i-1][j-k]
        res = []
        for i in range(n, n*6+1):
            res.append(float(dp[n][i])/6**n)
        return res