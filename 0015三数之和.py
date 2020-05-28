class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 排序+双指针遍历
        # https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
        n = len(nums)
        res=[]
        if not nums or n < 3:
            return res

        nums.sort()
        for i in range(n-2):
            # 如果当前数字已经大于0，那么后续数字没有必要遍历
            if nums[i] > 0:
                return res
            # 避免重复
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # 避免重复
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
                    
        return res