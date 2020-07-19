class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 递归
        # 参考官方题解
        # 时间复杂度O(n^3)，空间复杂度O(n^2)
        n = len(nums)
        val = [1] + nums + [1]
        
        @lru_cache(None) # 需要加这句才能通过
        def solve(left, right):
            if left >= right-1:
                return 0
            best = 0
            for i in range(left+1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            return best
        return solve(0, n+1)

        # 动态规划
        # 时间复杂度O(n^3)，空间复杂度O(n^2)
        n = len(nums)
        rec = [[0] * (n+2) for _ in range(n+2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i+2, n+2):
                for k in range(i+1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)
        
        return rec[0][n + 1]