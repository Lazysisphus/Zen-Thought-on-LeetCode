"""
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 

限制：

2 <= n <= 100000
"""

# 好困啊，但是只能晚上做题 (；′⌒`)

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # 方法1
        # 先将数组排序，然后顺次遍历
        # 时间复杂度O(nlogn)
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return nums[i]
        
        # 方法2
        # 使用一个哈希表来降低方法1的时间复杂度
        # 遍历数组，观察当前数字是否在哈希表中
        # 如果在，说明该数字重复，返回该数字
        # 时间复杂度O(n)，空间复杂度O(n)
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return num
            else:
                hash_map[num] = 0

        # 方法3
        # 利用数字都在0～n-1的特性
        # 遍历数组，如果当前数字cur_num等于当前下标，那么检查下一个数字
        # 如果当前数字cur_num不等于当前下标，那么判断cur_num是否等于cur_num位置上的数字
        #   如果相等，说明cur_num是一个重复数字，返回该数字
        #   如果不等，交换cur_num和cur_num下标位置的数字，直到当前下标和当前位置的数字相等
        # 时间复杂度O(n)，空间复杂度O(1)
        for i in range(len(nums)):
            cur_num = nums[i]
            while cur_num != i:
                if cur_num == nums[cur_num]:
                    return cur_num
                else:
                    nums[cur_num], nums[i] = nums[i], nums[cur_num]