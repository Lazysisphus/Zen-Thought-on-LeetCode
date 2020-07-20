class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 十进制数字异或规律：相同数字异或结果为0；0和任何数字异或，结果为该数字
        # 时间复杂度O(n)，空间复杂度O(1)
        xor_res = 0
        for num in nums: # 先计算所有数字异或的结果
            xor_res ^= num
        
        idx = 0
        while xor_res & 1 == 0: # 寻找最低位1所在的位数
            if xor_res & 1 != 1:
                xor_res >>= 1
                idx += 1
        
        r1, r2 = 0, 0
        for num in nums: # 根据idx位是否为1，将nums划分为两部分
            if (num >> idx) & 1 == 0:
                r1 ^= num
            else:
                r2 ^= num
        return [r1, r2]