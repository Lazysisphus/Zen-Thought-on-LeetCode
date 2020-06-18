# 在公司肝一道题！第三个解法也太妙了！都是怪物！
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法1：
        # 把原始数组的每一个元素都复制到一个哈希表中
        # 使用O(n)时间复杂度和O(n)空间复杂度，但是不符合题目要求

        # 方法2：
        # 抽屉原理+二分法，每次循环中二分区间，然后
        # 统计整个数组落在单边区间的数字的个数
        # 时间复杂度O(nlogn)，空间复杂度O(1)
        left = 1
        right = len(nums) - 1
        while left < right:
            cnt = 0
            mid = left + (right-left)//2
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left

        # 方法3：
        # 快慢指针：这个解法太妙了
        # 分为两步，第一步找到环中的某个点；第二步找到环的入口
        slow = 0
        fast = 0
        # 第一步
        slow = nums[slow]
        fast = nums[nums[fast]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # 第二步
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
