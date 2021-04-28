"""
633. 平方数之和
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

 

示例 1：

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：

输入：c = 3
输出：false
示例 3：

输入：c = 4
输出：true
示例 4：

输入：c = 2
输出：true
示例 5：

输入：c = 1
输出：true
 

提示：

0 <= c <= 231 - 1
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 可等价与二维矩阵上的搜索
        # 时间复杂度O(sqrt(c))
        # 参考题解：
        # https://leetcode-cn.com/problems/sum-of-square-numbers/solution/shuang-zhi-zhen-de-ben-zhi-er-wei-ju-zhe-ebn3/
        low, high = 0, int(sqrt(c))
        while low <= high:
            tmp_sum = low**2 + high ** 2
            if tmp_sum == c:
                return True
            elif tmp_sum < c:
                low += 1
            else:
                high -= 1
        return False