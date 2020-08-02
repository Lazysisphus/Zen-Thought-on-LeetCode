class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 方法1：循环自底向上实现
        if N == 0:
            return 0

        a, b = 0, 1
        while N:
            a, b = b, a+b
            N -= 1
        return a

        # 方法2：递归实现
        if N <= 1:
            return N
        else:
            return self.fib(N-1) + self.fib(N-2)

        # 方法3：记忆+递归
        # 占用空间会增多，但是速度会变快
        memory = {}
        def helper(N):
            # 记忆化部分
            if N in memory:
                return memory[N]
            # 递归部分
            if N <= 1:
                return N
            else:
                res = helper(N - 1) + helper(N - 2)
            memory[N] = res
            return res
        return helper(N)