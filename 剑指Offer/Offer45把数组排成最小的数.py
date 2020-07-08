class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 这道题的重点在于问题的转化
        # 通过证明可以得知，题目等价于对列表中所有的正整数按照一定的规则排序
        # 规则是，对于两个数字A和B，如果str(A)+str(B)<str(B)+str(A)
        # 那么定义A『小于』B，A需要排在B的前面
        # 借用题解区k姓大佬快排的方法，顺便学习下如何活用快排
        # 时间复杂度O(nlogn)，空间复杂度O(n)
        def fast_sort(l, r):
            if l >= r: 
                return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: 
                    j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: 
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            fast_sort(l, i-1)
            fast_sort(i+1, r)
        
        strs = [str(num) for num in nums]
        fast_sort(0, len(strs)-1)
        return ''.join(strs)