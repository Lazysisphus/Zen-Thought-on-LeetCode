class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        # 遍历
        for idx, num in enumerate(nums):
            if num == idx:
                return num
        return -1

        # 遍历的一点点优化，跳跃遍历
        i = 0
        while i < len(nums):
            if i == nums[i]:
                return i
            if i < nums[i]:
                i = nums[i]
            else:
                i += 1
        return -1