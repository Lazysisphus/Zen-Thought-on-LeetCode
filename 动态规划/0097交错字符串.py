class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # 动态规划
        # 注意dp二维矩阵中索引和各个字符串s中索引的不同含义
        # dp[i][j]表示长度为i+j的字符串可以由s1的前j个字符和s2的前i个字符交错而成
        # 而s1的前j个字符为s[: j-1]，s2也同理
        # 时间复杂度O(mn)，空间复杂度O(mn)，m、n分别是两个字符串的长度
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        
        dp = [[False] * (n2+1) for _ in range(n1+1)]
        dp[0][0] = True
        # 第0行
        for j in range(1, n2+1):
            dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])
        # 第0列
        for i in range(1, n1+1):
            dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        # print(dp)
        return dp[-1][-1]