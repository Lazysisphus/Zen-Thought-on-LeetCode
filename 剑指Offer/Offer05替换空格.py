"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 方法1
        # 使用额外空间存储新字符串
        # 时间和空间复杂度都是O(n)
        res = ''
        for ch in s:
            if ch == ' ':
                res += '%20'
            else:
                res += ch
        return res

        # 方法2（C语言）
        # 从前到后扫描字符串，每遇到一个空格，都将其后面的所有字符向后移动两个位置
        # 如果字符串长度为 n，平均有 n 个空格，每遇到一个空格移动 n 个字符
        # 那么时间复杂度为O(n^2)

        # 方法3
        # 首先统计字符串包含的空格数目，令新字符串长度为原字符串长度+2*空格数目
        # 然后使用双指针，从后到前扫描字符串
        # 指针p1指向原始字符串末尾，指针p2指向新字符串末尾
        # 如果p1当前指向字符不是空格，则将其直接移动到p2处，同时两个指针前移一个位置
        # 如果p1当前指向空格，则将p1前移一个位置，将p2前移三个位置，同时将“%20”补充在新字符串位置
        # 时间复杂度O(n)
        # python实现
        newS = s.replace(' ', '%20')
        return newS