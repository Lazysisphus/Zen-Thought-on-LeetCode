"""
368. 最大整除子集
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

 

示例 1：

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。
示例 2：

输入：nums = [1,2,4,8]
输出：[1,2,4,8]
 

提示：

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
nums 中的所有整数 互不相同
"""

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 动态规划，时间复杂度O(n^2)，空间复杂度O(n)
        # f[i]表示考虑nums前i个数字，且以nums[i]为子集最后一个数字时，子集的长度
        # 参考题解：
        # https://leetcode-cn.com/problems/largest-divisible-subset/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-0a3jc/
        nums.sort()
        n = len(nums)
        f, g = [0] * n, [0] * n
        for i in range(n):
            max_len, pre = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if f[j] + 1 > max_len:
                        max_len = f[j] + 1
                        pre = j
            f[i] = max_len
            g[i] = pre

        max_len, pos = -1, -1
        for i in range(n):
            if f[i] > max_len:
                max_len = f[i]
                pos = i
        
        ans = []
        while len(ans) < max_len:
            ans.append(nums[pos])
            pos = g[pos]
        ans = ans[::-1]
        return ans