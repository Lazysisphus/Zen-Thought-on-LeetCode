class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法1：自动机+每位状态分析
        # 时间复杂度O(n)，空间复杂度O(1)
        # 异或运算: x ^ 0 = x; x ^ 1 = ~x
        # 与运算：x & 1 = x; x ^ 0 = 0
        ones = 0
        twos = 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones

        # 方法2：常规解法，计算每一位对3求余的结果
        # 时间复杂度O(n)，空间复杂度O(1)
        res = 0
        for i in range(32):
            cnt = 0 # 记录当前 bit 有多少个1
            bit = 1 << i # 记录当前要操作的 bit
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于0说明唯一出现的数字在这个 bit 上是1
                res |= bit

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res