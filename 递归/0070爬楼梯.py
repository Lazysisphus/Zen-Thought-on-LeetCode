class Solution:
    def climbStairs(self, n: int) -> int:
        # 记忆+递归
        # 转换为斐波那契数列
        # f(0) = 0
        # f(1) = 1
        # f(2) = 2
        # f(3) = f(2) + f(1) = 3
        memory = {}
        def helper(n):
            if n in memory:
                return memory[n]
            if n <= 2:
                return n
            res = helper(n - 1) + helper(n - 2)
            memory[n] = res
            return res
        return helper(n)