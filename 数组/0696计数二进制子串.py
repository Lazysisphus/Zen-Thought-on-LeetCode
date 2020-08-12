class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 先统计连续的0和1分别有多少个，如：111100011000，得到4323；
        # 在4323中的任意相邻两个数字，取小的一个加起来，就是3 + 2 + 2 = 7
        # 下面的程序在空间上做了优化
        # 时间复杂度O(n)，空间复杂度O(1)
        cnt = 0
        pre = 0
        cur = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                pre = cur
                cur = 1
            if pre >= cur: # pre是配对数的上限
                cnt += 1
        return cnt