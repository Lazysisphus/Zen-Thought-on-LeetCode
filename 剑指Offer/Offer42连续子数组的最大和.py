class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 经典动态规划题目
        # 时间复杂度O(n)
        # dp[i]表示以nums[i]作为结尾的连续子数组的最大和
        # 如果dp[i-1] < 0，那么dp[i] = nums[i]
        # 如果dp[i-1] >= 0，那么dp[i] = dp[i-1] + nums[i]
        n = len(nums)
        dp_i = max_sum = nums[0]
        for i in range(1, n):
            dp_i = max(dp_i + nums[i], nums[i]) # 状态转移方程
            max_sum = max(dp_i, max_sum) # max_sum用于记录最大的dp_i
        return max_sum