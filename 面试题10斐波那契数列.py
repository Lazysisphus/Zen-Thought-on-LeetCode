# 今天也很困呢 (ఠ్ఠ ˓̭ ఠ్ఠ)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 方法1：递归，超出时间限制
        def helper(n):
            if n <= 1:
                return n
            else:
                return helper(n-2)+helper(n-1)
        ans = helper(n)
        ans = ans % 1000000007
        return ans

        # 方法2：循环，时间复杂度O(n)，空间复杂度O(n)
        res = []
        for i in range(n+1):
            if i == 0 or i == 1:
                res.append(i)
            else:
                res.append(res[i-2] + res[i-1])
        return res[-1] % 1000000007

        # 方法3：循环，时间复杂度O(n)，空间复杂度O(1)
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a % 1000000007
