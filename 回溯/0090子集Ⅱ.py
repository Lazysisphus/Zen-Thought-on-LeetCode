class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 经典回溯
        res = []
        n = len(nums)
        nums.sort()
        def dfs(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                dfs(j + 1, tmp + [nums[j]])
        dfs(0, [])
        return res