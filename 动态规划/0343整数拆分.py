class Solution:
    def integerBreak(self, n: int) -> int:
        # 方法1：动态规划
        # 令dp[i]表示正整数i拆分后，拆分项的最大乘积
        # dp[0] = dp[1] = 0
        # dp[i] = max(j * (i-j), j * dp[i-j])
        # 时间复杂度O(n^2)，空间复杂度O(n)
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i-j])
        return dp[n]

        # 方法2：数学推导 + 贪心
        # 应该尽量多截取长度为3的小段
        # 时间复杂度O(n)（需要使用math.pow()），空间复杂度O(n)
        if n < 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return math.pow(3, a)
        if b == 1:
            return math.pow(3, a - 1) * 4
        if b == 2:
            return math.pow(3, a) * 2