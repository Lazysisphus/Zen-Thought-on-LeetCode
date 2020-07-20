class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        # 动态规划的思想，使用两个列表分别保存左侧的连乘结果和右侧的连乘结果来避免重复的计算
        # 时间复杂度O(n)，空间复杂度O(n)
        n = len(a)
        left, right = [1 for _ in range(n)], [1 for _ in range(n)]
        for i in range(1, n):
            left[i] = left[i-1] * a[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * a[i+1]
        for i in range(n):
            left[i] = left[i] * right[i]
        return left