class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 抄了抄作业，很贴心的一道题
        # 时间复杂度O(nlogn)，空间复杂度O(1)
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: 
                joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: 
                return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子