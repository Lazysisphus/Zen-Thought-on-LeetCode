'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i, tmp):
            if len(tmp) == k:
                res.append(tmp)
                return
            for j in range(i, n + 1):
                backtrack(j + 1, tmp + [j])

        res = []
        backtrack(1, [])
        return res