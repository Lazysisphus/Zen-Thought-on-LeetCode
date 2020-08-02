class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dfs + memory
        def dfs(idx, cur_sum):
            if idx == len(nums):
                if cur_sum == S:
                    return 1
                else:
                    return 0
            if (idx, cur_sum) in memory:
                res = memory[(idx, cur_sum)]
            else:
                res = dfs(idx+1, cur_sum+nums[idx]) + dfs(idx+1, cur_sum-nums[idx])
                memory[(idx, cur_sum)] = res
            return res

        if not nums:
            return 0
        memory = {}
        return dfs(0, 0)