class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 经典回溯
        # 在for循环中，只要当前遍历到的字符和上一个字符相同，那么跳过当前字符
        # 相当于做了剪枝
        res = []
        nums.sort() # 得排序!!!
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[: i] + nums[i + 1: ], tmp + [nums[i]])
        backtrack(nums, [])
        return res