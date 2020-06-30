class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 题解区大佬的动态规划
        # 从最小的丑数开始递推，下一个丑数必定来自已有的丑数
        # 已有丑数*2、*3和*5后，刚好大于目前最大的丑数
        # 然后从三个备选丑数中选择最小的一个作为下一个丑数
        # 关键点：使用a、b和c记录使用哪些已有丑数来产生备选丑数
        # 时间复杂度O(n)，空间复杂度O(n)
        dp = [1 for _ in range(n)]
        a, b, c = 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2, n3, n5)
            if n2 == dp[i]:
                a += 1
            if n3 == dp[i]:
                b += 1
            if n5 == dp[i]:
                c += 1
        return dp[-1]