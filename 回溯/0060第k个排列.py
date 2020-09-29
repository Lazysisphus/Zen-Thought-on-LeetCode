'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 抄一下作业，这个系列都怪难
        # https://leetcode-cn.com/problems/permutation-sequence/solution/hui-su-jian-zhi-python-dai-ma-java-dai-ma-by-liwei/
        def dfs(idx):
            nonlocal n, k
            if idx == n:
                return
            cnt = element[n - idx - 1]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                res.append(i)
                used[i] = True
                dfs(idx + 1)
                return 

        if n == 0:
            return ""
        res = []
        used = [False for _ in range(n + 1)]
        element = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            element[i] = element[i - 1] * i
        dfs(0)
        return "".join([str(x) for x in res])