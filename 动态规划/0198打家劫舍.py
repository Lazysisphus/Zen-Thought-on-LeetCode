class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp
        # 时间复杂度O(n)，空间复杂度O(n)
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

        # dp，优化空间复杂度方法1
        # 时间复杂度O(n)，空间复杂度O(1)
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2, n):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        return nums[-1]

        # dp，优化空间复杂度方法2
        # 时间复杂度O(n)，空间复杂度O(1)
        pre = 0
        cur = 0
        # 循环开始时，cur 表示 dp[k-1]，pre 表示 dp[k-2]
        for num in nums:
            # dp[k] = max(dp[k-1], dp[k-2] + i)
            tmp = max(cur, pre + num)
            pre = cur
            cur = tmp
            # 循环结束时，cur 表示 dp[k]，prev 表示 dp[k-1]
        return cur