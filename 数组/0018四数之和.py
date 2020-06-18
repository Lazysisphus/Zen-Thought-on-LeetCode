class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 外面的两层循环固定两个数字，内层的while循环使用双指针查找
        # 下面题解思路总体正确，稍有错误
        # https://leetcode-cn.com/problems/4sum/solution/gu-ding-liang-ge-shu-yong-shuang-zhi-zhen-zhao-lin/
        res = []
        n = len(nums)
        if n == 0 or n < 4: 
            return res

        nums.sort()
        for i in range(n-3):
            # 防止重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 当数组最小值和都大于target，跳出
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break

            for j in range(i+1, n-2):
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res
        