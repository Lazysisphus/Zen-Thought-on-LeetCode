class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 转换为0-1背包问题
        # 根据示例列出表达式，可以发现，题目转化为将石头分成两堆，使两堆的差最小
        # 那么可以进一步理解为，挑选出一组石头，使他们在容量为总重一半的背包中最重
        # 使用动态规划
        # dp数组的行数为石头数量+1，列数为比石头总重一半稍大的整数+1
        # 时间复杂度O(mn)，空间复杂度O(mn)
        row = len(stones)
        col = int(sum(stones) / 2.0) + 1
        
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if stones[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i - 1]] + stones[i - 1])
        return sum(stones) - 2 * dp[-1][-2]