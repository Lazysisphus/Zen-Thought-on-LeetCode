class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 参考官方解答，使用递归和迭代两种方式实现快速幂
        # 递归，时间复杂度O(logn)，空间复杂度O(logn)
        def helper(N):
            if N == 0:
                return 1.0
            y = helper(N // 2)
            if N % 2 == 1:
                return y * y * x
            else:
                return y * y
        return helper(n) if n >= 0 else 1.0 / helper(-n)

        # 迭代，时间复杂度O(logn)，空间复杂度O(1)
        def helper(N):
            ans = 1.0
            x_contribute = x
            while N:
                if N % 2 == 1:
                    ans *= x_contribute
                x_contribute *= x_contribute
                N //= 2
            return ans
        return helper(n) if n >= 0 else 1.0 / helper(-n)