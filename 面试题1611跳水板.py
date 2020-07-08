class Solution(object):
    def divingBoard(self, shorter, longer, k):
        """
        :type shorter: int
        :type longer: int
        :type k: int
        :rtype: List[int]
        """
        # 处理好特殊情况，即k<=0以及shorter==longer
        # 时间复杂度O(n)
        if k <= 0: 
            return []
        # 特殊情况加速处理
        if shorter == longer: 
            return [shorter * k]
        # 长短版的数量随k变化而变化，当 shorter != longer时，会有k+1个不同的结果
        ans = []
        for i in range(k + 1):
            ans.append(shorter * (k - i) + longer * i)
        return ans