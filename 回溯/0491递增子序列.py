class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 带条件的dfs
        res = []
        def dfs(nums, tmp):
            if len(tmp) > 1:
                res.append(tmp)
            curPres = {}
            for idx, i in enumerate(nums):
                if i in curPres:
                    continue
                if not tmp or i >= tmp[-1]:
                    curPres[i] = 0
                    dfs(nums[idx+1: ], tmp+[i])

        dfs(nums, [])
        return res