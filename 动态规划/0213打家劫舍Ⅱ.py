class Solution:
    def rob(self, nums: List[int]) -> int:
        # 偷第一个房间不偷最后一个房间，或者反之
        # 转换成两个子问题，保证首尾两个房子不能同时偷窃
        # 时间复杂度O(n)，空间复杂度O(1)
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        pre = 0 # dp[i - 2]
        cur = 0 # dp[i - 1]
        for i in nums[: -1]:
            tmp = max(cur, pre + i)
            pre = cur
            cur = tmp
        ans1 = cur

        pre = 0
        cur = 0
        for i in nums[1: ]:
            tmp = max(cur, pre + i)
            pre = cur
            cur = tmp
        ans2 = cur
        ans = max(ans1, ans2)
        return ans