class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 递归+回溯
        # first：表示从first及之后的范围内选择一个元素作为当前的元素
        # 时间复杂度O(kC(nk))，空间复杂度O(C(nk))，括号内分别是组合数的下标和上标
        def backtrack(first, curr):
            if len(curr) == k:
                import copy 
                output.append(copy.copy(curr))
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop() # 回溯
        
        output = []
        backtrack(1, [])
        return output