class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 从两侧向中间寻找
        # 当遇到第一对不相同的字符时，判断左侧+1或者右侧-1后对应的字符串是否回文
        # 如果两个子串都不是回文字符串，说明只修改一次无法得到回文字符串
        if s == s[:: -1]:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                sub_a = s[l + 1: r + 1]
                sub_b = s[l: r]
                return sub_a == sub_a[:: -1] or sub_b == sub_b[:: -1]