class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法1：动态规划
        # 动态规划的4个特点：
        # 1.求问题的最优解
        # 2.整体问题的最优解依赖各个子问题的最优解
        # 3.将大问题分解成小问题之后，小问题之间还有相互重叠的更小的子问题
        # 4.从上往下分析问题，从下往上求解问题
        # 本题使用动态规划，时间复杂度O(n^2)，空间复杂度O(n)
        dp = [0 for _ in range(n+1)]
        dp[2] = 1 # dp[0]、dp[1]不满足题意，不需要求解
        for i in range(3, n+1):
            for j in range(i):
                # dp[i]：不剪
                # j*(i-j)：剪下i-j，i-j不再剪
                # j*dp[i-j]：剪下i-j，i-j继续剪
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        
        return dp[n]

        # 方法2：数学证明 + 贪心
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