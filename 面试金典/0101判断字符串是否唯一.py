tTime: 2021-04-16 17:17:41
"""
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false 
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-unique-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isUnique(self, astr: str) -> bool:
        # 利用位运算，实现O(n)时间复杂度以及O(1)空间复杂度
        # 步骤：
        #   设置变量memory，用于记忆某个字符有没有出现过，可看作26位二进制数字
        #   遍历字符串中的每一个字符，计算得到该字符在memory中对应的位置（1<<pos），将那个位置置“1”
        #   如果memory和(1<<pos)相与不为0，那么说明当前遍历到的字符出现过，返回False
        #   遍历中需要更新memory
        memory = 0 
        for ch in astr:
            pos = ord(ch) - ord("a")
            if memory & (1 << pos) != 0:
                return False
            else:
                memory = memory | (1 << pos)
        return True