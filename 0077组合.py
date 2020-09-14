class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 递归+回溯
        # i：表示从 i 及之后的范围内选择一个元素作为当前的元素
        # 时间复杂度O(kC(nk))，空间复杂度O(C(nk))，括号内分别是组合数的下标和上标
        def backtrack(i, tmp):
            if len(tmp) == k:
                res.append(tmp[:])
            for j in range(i, n + 1):
                tmp.append(j)
                backtrack(j + 1, tmp)
                tmp.pop() # 回溯
        
        res = []
        backtrack(1, [])
        return res