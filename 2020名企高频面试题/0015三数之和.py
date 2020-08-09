class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 排序+双指针遍历
        # 遍历整个数组，在每次遍历中：
        #   如果当前数字大于0，那么后续无需遍历，直接返回res
        #   如果当前数字和前一个数字相同，为了去重，直接进行下次遍历
        #   否则，取当前数字后面的一个数字作为left，取最右侧数字作为right
        #       当左右两个指针没有相遇，判断i、left、right三个指针指向数字之和与0的关系，同时在此过程中去重
        # 时间复杂度O(n^2)，空间复杂度O(1)
        n = len(nums)
        if not nums or n < 3:
            return []
        
        res = []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res