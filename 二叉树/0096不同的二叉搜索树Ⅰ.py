class Solution:
    def numTrees(self, n: int) -> int:
        # dp
        # 时间复杂度O(n^2)，空间复杂度O(n)
        # G(n) 表示长度为 n 的序列可以构造的二叉搜索树的个数
        # F(i, n) 表示以 i 为根结点的长度为 n 的序列可以构造的二叉搜索树的个数
        # 那么G(n)=sum(F(i, n), i in [1, n])，F(i, n)=G(i-1)*G(n-i)
        # 因此G(n)=sum(G(i-1)*G(n-i), i in [1, n])
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]

        # 卡特兰数
        # G(n) = 2*(2*n+1)*G(n-1) / (n+2)
        # 时间复杂度O(n)，空间复杂度O(1)
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)