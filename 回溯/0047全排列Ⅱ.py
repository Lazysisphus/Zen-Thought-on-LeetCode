'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 在for循环中，只要当前遍历到的字符和上一个字符相同，那么跳过当前字符
        # 相当于做了剪枝
        res = []
        nums.sort() # 得排序!!!
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[: i] + nums[i + 1: ], tmp + [nums[i]])
        backtrack(nums, [])
        return res